"""Offline audit evidence must not become permission, fresh scope, or a leak."""
import copy
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from email.message import Message
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.request import Request

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import refresh_program_scopes as refresh

URL = 'https://bugcrowd.com/engagements/example'
BRIEF = URL + '/changelog/version.json'
PAGE = '{"getBriefVersionDocument":"/engagements/example/changelog/version"}'
BODY = {'data': {'scope': [{'name': 'In scope', 'inScope': True,
                          'targets': [{'name': 'example.test', 'category': 'website', 'uri': None}]}]}}
H1 = 'https://hackerone.com/example'
H1_SOURCE = 'https://hackerone.com/teams/example/assets/download_csv.csv'
CSV_HEADER = ('identifier,asset_type,instruction,eligible_for_bounty,eligible_for_submission,'
              'availability_requirement,confidentiality_requirement,integrity_requirement,'
              'max_severity,system_tags,created_at,updated_at\n')
INTIGRITI = 'https://app.intigriti.com/programs/example/public'
SECRET = 'sensitive-token-DO-NOT-LOG'


class Client:
    def __init__(self, responses):
        self.responses, self.calls = responses, []

    def get(self, url):
        self.calls.append(url)
        response = self.responses[url]
        if isinstance(response, Exception):
            raise response
        return response


class AuditInstrumentationTests(unittest.TestCase):
    def run_fixture(self, client, platform='Bugcrowd', url=URL, overlap=False, record=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'data/programs').mkdir(parents=True)
            capture = record or {'program_url': url, 'platform': platform, 'status': 'captured',
                                 'captured_at': '2026-10-03T00:00:00Z',
                                 'assets': [{'name': 'example.test', 'scope': 'in', 'asset_type': 'website',
                                             'location': None, 'group': 'In scope'}]}
            for name, rows in zip(refresh.CAPTURES, [[capture], []]):
                refresh.dump(root / name, {'captures': rows})
            if overlap:
                policy = {'program_url': url, 'platform': platform, 'last_verified_at': '2026-10-03T00:00:00Z',
                          'sources': [{'id': 'scope', 'url': url}],
                          'asset_scope': {'source_ids': ['scope'], 'verified_at': '2026-10-03T00:00:00Z',
                                          'in_scope': [{'name': 'example.test', 'asset_type': 'website',
                                                        'note': 'A qualification requiring manual review',
                                                        'source_ids': ['scope']}], 'out_of_scope': []}}
                refresh.dump(root / 'data/programs/example.json', policy)
            before = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*.json')}
            with patch('socket.socket', side_effect=AssertionError('Network is forbidden in this test')):
                audit = refresh.refresh(root, client)
            after = {name: (root / name).read_bytes() for name in before}
            return audit, before, after

    def failure(self, client, **kwargs):
        audit, before, after = self.run_fixture(client, **kwargs)
        self.assertEqual(before, after, 'Failure must preserve every canonical byte and date')
        self.assertEqual(audit['counts'], {'refreshed': 0, 'failed': 1, 'deferred': 0,
                                         'unsupported': 0, 'total': 1, 'attempted': 1})
        self.assertEqual(audit['results'][0]['verification_status'], 'unknown')
        return audit['results'][0]

    def test_partial_http_response_cannot_be_parsed_or_advance_scope(self):
        class Response(io.BytesIO):
            def __init__(self, body, status=200, ranged=False):
                super().__init__(body.encode())
                self.status, self.read_called = status, False
                self.headers = Message()
                self.headers['Content-Length'] = str(len(body.encode()))
                if ranged:
                    self.headers['Content-Range'] = SECRET
            def getcode(self): return self.status
            def read(self, *args):
                self.read_called = True
                return super().read(*args)
        for status, ranged in ((206, True), (206, False), (200, True), (204, False), (201, False)):
            calls = []
            partial = Response(json.dumps(BODY), status, ranged)
            class Opener:
                def open(self, request, timeout):
                    calls.append(request.full_url)
                    return Response(PAGE) if request.full_url == URL else partial
            client = refresh.PublicClient(); client.opener = Opener()
            with self.subTest(status=status, ranged=ranged), patch.object(refresh.time, 'sleep'):
                result = self.failure(client, overlap=True)
                self.assertEqual(result['reason_code'], 'http_response_incomplete')
                self.assertEqual(result['http_status'], status)
                self.assertEqual(result['failed_source_url'], BRIEF)
                self.assertEqual(calls, [URL, BRIEF])
                self.assertFalse(partial.read_called)
                self.assertTrue(partial.closed)
                self.assertNotIn(SECRET, json.dumps(result))

    def test_complete_200_without_content_range_is_accepted(self):
        class Response(io.BytesIO):
            def __init__(self, body):
                super().__init__(body.encode())
                self.headers = Message()
                self.headers['Content-Length'] = str(len(body.encode()))
            def getcode(self): return 200
        class Opener:
            def open(self, request, timeout):
                return Response(PAGE if request.full_url == URL else json.dumps(BODY))
        client = refresh.PublicClient(); client.opener = Opener()
        with patch.object(refresh.time, 'sleep'):
            audit, _, _ = self.run_fixture(client)
        self.assertEqual(audit['counts']['refreshed'], 1)
        self.assertEqual(audit['counts']['failed'], 0)

    def test_all_redacted_brief_is_not_a_fresh_usable_scope(self):
        body = copy.deepcopy(BODY)
        body['data']['scope'][0]['targets'][0]['name'] = '██████'
        result = self.failure(Client({URL: PAGE, BRIEF: json.dumps(body)}))
        self.assertEqual(result['reason_code'], 'bugcrowd_scope_redacted')
        self.assertEqual(result['observation_status'], 'redacted_public_table')
        self.assertEqual(result['observed_redacted_asset_count'], 1)
        self.assertEqual(result['observed_non_redacted_asset_count'], 0)
        self.assertEqual(result['observation_source_url'], BRIEF)
        self.assertRegex(result['response_sha256'], '^[a-f0-9]{64}$')
        self.assertNotIn('████', json.dumps(result, ensure_ascii=False))

    def test_mixed_redacted_rows_and_visible_locations_are_not_erased(self):
        for targets in ([{'name': '████', 'category': 'website', 'uri': 'https://example.test'}],
                        [{'name': '████', 'category': 'website', 'uri': None},
                         {'name': 'example.test', 'category': 'website', 'uri': None}]):
            body = copy.deepcopy(BODY)
            body['data']['scope'][0]['targets'] = targets
            parsed = refresh.parse_brief(URL, PAGE, lambda source: json.dumps(body))
            self.assertEqual(len(parsed['assets']), len(targets))
            self.assertEqual([x['name'] for x in parsed['assets']], [x['name'] for x in targets])

    def test_redacted_count_cannot_leak_untrusted_details(self):
        for count in (SECRET, True, -1, None):
            error = refresh.ObservationError('bugcrowd_scope_redacted', observed_redacted_asset_count=count,
                                             response_body=SECRET)
            result = refresh.failure_fields(error, 'response_parse', BRIEF)
            self.assertNotIn('observed_redacted_asset_count', result)
            self.assertNotIn(SECRET, json.dumps(result))

    def test_migration_redirect_is_classified_without_following_it(self):
        client = Client({URL: refresh.ObservationError('redirect_requires_review', http_status=302,
                        redirect_category=refresh.redirect_category(URL, URL + '/migrated?token=' + SECRET))})
        result = self.failure(client)
        self.assertEqual(result['redirect_category'], 'same_program_migration_route')
        self.assertEqual(client.calls, [URL])
        self.assertNotIn(SECRET, json.dumps(result))
        self.assertEqual(refresh.redirect_category(URL, URL + '-other/migrated'), 'same_origin_other_route')

    def test_404_records_exact_requested_brief_not_error_url_or_headers(self):
        error = HTTPError('https://other.test/' + SECRET + '?token=' + SECRET, 404, SECRET,
                          {'Location': SECRET, 'Set-Cookie': SECRET}, io.BytesIO(SECRET.encode()))
        result = self.failure(Client({URL: PAGE, BRIEF: error}))
        self.assertEqual(result['failed_source_url'], BRIEF)
        self.assertEqual(result['http_status'], 404)
        self.assertEqual(result['failure_stage'], 'source_request')
        self.assertEqual(result['reason_code'], 'http_error')
        self.assertNotIn(SECRET, json.dumps(result))
        self.assertNotIn('closed', json.dumps(result))

    def test_landing_404_is_distinct_from_selected_brief(self):
        client = Client({URL: HTTPError(URL, 404, 'not found', {}, None)})
        result = self.failure(client)
        self.assertEqual(result['failed_source_url'], URL)
        self.assertEqual(client.calls, [URL])

    def test_safe_audit_url_omits_query_fragment_and_never_relaxes_request_validation(self):
        polluted = BRIEF + '?token=' + SECRET + '#' + SECRET
        self.assertEqual(refresh.safe_audit_source(polluted), BRIEF)
        with self.assertRaises(ValueError):
            refresh.official_url(polluted)
        result = refresh.failure_fields(HTTPError(polluted, 404, SECRET, {}, None), 'source_request', polluted)
        self.assertEqual(result['failed_source_url'], BRIEF)
        self.assertNotIn(SECRET, json.dumps(result))

    def test_unapproved_credential_and_encoded_path_urls_are_not_recorded(self):
        unsafe = ['https://user:' + SECRET + '@bugcrowd.com/engagements/example',
                  'https://evil.test/' + SECRET, BRIEF + '\n' + SECRET,
                  URL + '/%2F' + SECRET, 'https://bugcrowd.com:443/engagements/example',
                  'https://bugcrowd.com/engagements/fmshrc-vdp/changelog/version.json']
        for source in unsafe:
            with self.subTest(source=source):
                self.assertIsNone(refresh.safe_audit_source(source))
                result = refresh.failure_fields(ValueError(SECRET), 'source_request', source)
                self.assertNotIn('failed_source_url', result)
                self.assertNotIn(SECRET, json.dumps(result))

    def test_transport_and_unexpected_errors_cannot_leak_messages(self):
        for error in (URLError(SECRET), TimeoutError(SECRET), RuntimeError(SECRET),
                      ValueError('Scope group schema changed ' + SECRET), KeyError(SECRET)):
            with self.subTest(error=type(error).__name__):
                result = self.failure(Client({URL: error}))
                self.assertNotIn(SECRET, json.dumps(result))

    def test_nofollow_redirect_has_only_route_category_and_status(self):
        calls = []
        class Opener:
            def open(self, request, timeout):
                calls.append(request.full_url)
                return refresh.NoRedirect().redirect_request(
                    request, None, 302, SECRET, {'Set-Cookie': SECRET},
                    INTIGRITI + '/preview/detail?token=' + SECRET + '#' + SECRET)
        client = refresh.PublicClient()
        client.opener = Opener()
        with patch.object(refresh.time, 'sleep'):
            result = self.failure(client, platform='Intigriti', url=INTIGRITI)
        self.assertEqual(calls, [INTIGRITI + '/detail'])
        self.assertEqual(result['redirect_category'], 'same_program_preview_route')
        self.assertEqual(result['observation_status'], 'redirect_not_followed')
        self.assertEqual(result['http_status'], 302)
        self.assertEqual(result['failed_source_url'], INTIGRITI + '/detail')
        self.assertNotIn('gate', json.dumps(result))
        self.assertNotIn(SECRET, json.dumps(result))

    def test_relative_terms_redirect_and_other_destinations_remain_no_follow(self):
        source = INTIGRITI + '/detail'
        destinations = {
            'tac/detail?token=' + SECRET: 'same_program_terms_route',
            source: 'same_program_scope_route',
            'https://app.intigriti.com/programs/other/program/preview/detail?token=' + SECRET: 'same_origin_other_route',
            'https://other.test/' + SECRET: 'cross_origin',
            'http://app.intigriti.com/programs/example/public/tac/detail': 'unsafe_or_unrecognized',
            'https://user:' + SECRET + '@app.intigriti.com/programs/example/public/tac/detail': 'unsafe_or_unrecognized',
            'https://app.intigriti.com:443/programs/example/public/tac/detail': 'unsafe_or_unrecognized',
            'https://app.intigriti.com/programs/example/public/tac/detail\n' + SECRET: 'unsafe_or_unrecognized',
            'https://app.intigriti.com/' + 'x' * 4100: 'unsafe_or_unrecognized',
        }
        for destination, expected in destinations.items():
            with self.subTest(expected=expected):
                with self.assertRaises(refresh.ObservationError) as caught:
                    refresh.NoRedirect().redirect_request(Request(source), None, 307, SECRET, {}, destination)
                result = refresh.failure_fields(caught.exception, 'source_request', source)
                self.assertEqual(result['redirect_category'], expected)
                self.assertNotIn(SECRET, json.dumps(result))

    def test_untrusted_observation_details_are_allowlisted(self):
        error = refresh.ObservationError('redirect_requires_review', redirect_category=[SECRET],
                                         http_status=SECRET, response_sha256=SECRET, response_body=SECRET,
                                         destination_url=SECRET)
        result = refresh.failure_fields(error, SECRET, None)
        self.assertEqual(result['redirect_category'], 'unsafe_or_unrecognized')
        self.assertEqual(result['failure_stage'], 'unknown')
        self.assertNotIn(SECRET, json.dumps(result))

    def test_redirect_handler_intercepts_unsafe_schemes_missing_and_duplicate_locations(self):
        request = Request(INTIGRITI + '/detail')
        cases = [('file:///' + SECRET,), ('javascript:' + SECRET,), (),
                 (INTIGRITI + '/preview/detail', 'https://other.test/' + SECRET)]
        for values in cases:
            headers = Message()
            for value in values:
                headers.add_header('Location', value)
            body = io.BytesIO(SECRET.encode())
            with self.assertRaises(refresh.ObservationError) as caught:
                refresh.NoRedirect().http_error_302(request, body, 302, SECRET, headers)
            self.assertTrue(body.closed)
            result = refresh.failure_fields(caught.exception, 'source_request', request.full_url)
            self.assertEqual(result['redirect_category'], 'unsafe_or_unrecognized')
            self.assertEqual(result['observation_status'], 'redirect_not_followed')
            self.assertNotIn(SECRET, json.dumps(result))

    def test_every_supported_redirect_status_stops_without_reading_body(self):
        class NoRead(io.BytesIO):
            def read(self, *args):
                raise AssertionError('A redirect body must not be read')
        for code in (301, 302, 303, 307, 308):
            body = NoRead(SECRET.encode())
            with self.assertRaises(refresh.ObservationError) as caught:
                getattr(refresh.NoRedirect(), 'http_error_' + str(code))(
                    Request(INTIGRITI + '/detail'), body, code, SECRET,
                    {'Location': INTIGRITI + '/tac/detail?token=' + SECRET})
            result = refresh.failure_fields(caught.exception, 'source_request', INTIGRITI + '/detail')
            self.assertEqual(result['redirect_category'], 'same_program_terms_route')
            self.assertEqual(result['http_status'], code)
            self.assertTrue(body.closed)
            self.assertNotIn(SECRET, json.dumps(result))

    def test_bugcrowd_explicit_empty_structure_has_evidence_and_stays_failed(self):
        for document in ({'data': {'scope': []}},
                         {'data': {'scope': [{'name': 'In scope', 'inScope': True, 'targets': []}]}}):
            raw = json.dumps(document)
            result = self.failure(Client({URL: PAGE, BRIEF: raw}))
            self.assertEqual(result['reason_code'], 'bugcrowd_scope_empty')
            self.assertEqual(result['observation_status'], 'empty_public_table')
            self.assertEqual(result['observed_asset_count'], 0)
            self.assertEqual(result['response_sha256'], hashlib.sha256(raw.encode()).hexdigest())
            self.assertEqual(result['observation_source_url'], BRIEF)
            self.assertNotIn('failed_source_url', result)

    def test_missing_malformed_groups_and_json_never_become_confirmed_empty(self):
        raw_documents = ['{broken ' + SECRET, 'null', '[]', '{}',
                         json.dumps({'data': None}), json.dumps({'data': {}}),
                         json.dumps({'data': {'scope': None}}), json.dumps({'data': {'scope': {}}})]
        for raw in raw_documents:
            result = self.failure(Client({URL: PAGE, BRIEF: raw}))
            self.assertEqual(result['reason_code'], 'bugcrowd_scope_schema_invalid')
            self.assertEqual(result['observation_status'], 'invalid_source_response')
            self.assertNotIn('observed_asset_count', result)
            self.assertNotIn(SECRET, json.dumps(result))

    def test_invalid_group_target_and_publication_values_never_become_empty(self):
        documents = [{'data': {'scope': [None]}}, {'data': {'scope': [{}]}},
                     {'data': {'scope': [{'name': 'scope', 'inScope': True, 'targets': [None]}]}},
                     {'data': {'scope': []}, 'publishedAt': {'private': SECRET}}]
        for document in documents:
            result = self.failure(Client({URL: PAGE, BRIEF: json.dumps(document)}))
            self.assertNotEqual(result['observation_status'], 'empty_public_table')
            self.assertNotIn('observed_asset_count', result)
            self.assertNotIn(SECRET, json.dumps(result))

    def test_hackerone_header_only_is_empty_but_wrong_schema_is_not(self):
        result = self.failure(Client({H1_SOURCE: CSV_HEADER}), platform='HackerOne', url=H1)
        self.assertEqual(result['reason_code'], 'hackerone_scope_empty')
        self.assertEqual(result['response_sha256'], hashlib.sha256(CSV_HEADER.encode()).hexdigest())
        for raw in ('identifier,wrong\n', CSV_HEADER.rstrip('\n'), CSV_HEADER + 'broken\n'):
            result = self.failure(Client({H1_SOURCE: raw}), platform='HackerOne', url=H1)
            self.assertNotEqual(result['observation_status'], 'empty_public_table')
            self.assertNotIn('observed_asset_count', result)

    def test_intigriti_zero_row_loading_and_login_shells_remain_unverified(self):
        source = INTIGRITI + '/detail'
        for content in ('', '<div>Loading...</div>', '<div>Please sign in to view scope</div>'):
            raw = '<lib-assets-detail>' + content + '</lib-assets-detail>'
            result = self.failure(Client({source: raw}), platform='Intigriti', url=INTIGRITI)
            self.assertEqual(result['reason_code'], 'intigriti_no_visible_rows')
            self.assertEqual(result['observation_status'], 'unverified_no_rows_observed')
            self.assertEqual(result['response_sha256'], hashlib.sha256(raw.encode()).hexdigest())
            self.assertNotIn('observed_asset_count', result)
        for malformed in ('login ' + SECRET, '<lib-assets-detail>'):
            result = self.failure(Client({source: malformed}), platform='Intigriti', url=INTIGRITI)
            self.assertNotEqual(result['observation_status'], 'empty_public_table')
            self.assertNotIn(SECRET, json.dumps(result))

    def test_record_update_rejection_preserves_overlap_and_policy_dates(self):
        result = self.failure(Client({URL: PAGE, BRIEF: json.dumps(BODY)}), overlap=True)
        self.assertEqual(result['reason_code'], 'curated_qualifications_require_review')
        self.assertEqual(result['failure_stage'], 'record_update')
        self.assertEqual(result['observation_status'], 'record_update_rejected')
        self.assertNotIn('failed_source_url', result)
        self.assertNotIn('observation_source_url', result)

    def test_invalid_brief_identity_is_not_attributed_to_a_failed_fetch(self):
        client = Client({URL: PAGE.replace('/engagements/example/', '/engagements/other/')})
        result = self.failure(client)
        self.assertEqual(client.calls, [URL])
        self.assertEqual(result['reason_code'], 'current_brief_identity_mismatch')
        self.assertEqual(result['observation_source_url'], URL)
        self.assertNotIn('failed_source_url', result)

    def test_403_429_still_stop_the_platform_and_retain_data(self):
        for code in (401, 403, 429):
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / 'data/programs').mkdir(parents=True)
                rows = [{'program_url': URL + str(i), 'platform': 'Bugcrowd', 'captured_at': 'old', 'assets': []}
                        for i in range(3)]
                for name, captures in zip(refresh.CAPTURES, [rows, []]):
                    refresh.dump(root / name, {'captures': captures})
                before = (root / refresh.CAPTURES[0]).read_bytes()
                client = Client({r['program_url']: HTTPError(r['program_url'] + '?token=' + SECRET, code, SECRET, {}, None)
                                 for r in rows})
                result = refresh.refresh(root, client)
                self.assertEqual(len(client.calls), 1)
                self.assertEqual(result['counts']['failed'], 1)
                self.assertEqual(result['counts']['deferred'], 2)
                self.assertEqual(before, (root / refresh.CAPTURES[0]).read_bytes())
                self.assertNotIn(SECRET, json.dumps(result))

    def test_all_exclusions_remain_zero_request_with_unchanged_data(self):
        urls = ['https://bugcrowd.com/engagements/' + name for name in ('fmshrc-vdp', 'abmc-vdp', 'oshrc-vdp')]
        urls += ['https://eu.bugcrowd.net/engagements/' + name for name in ('Demo-EU-admin-Test', 'demo-eu-admin-pentest-max-4')]
        for url in urls:
            client = Client({})
            audit, before, after = self.run_fixture(client, url=url)
            self.assertEqual(client.calls, [])
            self.assertEqual(before, after)
            self.assertEqual(audit['results'][0]['reason_code'], 'source_excluded')
            self.assertEqual(audit['counts']['attempted'], 0)

    def test_success_still_updates_only_scope_and_keeps_count_semantics(self):
        client = Client({URL: PAGE, BRIEF: json.dumps(BODY)})
        audit, before, after = self.run_fixture(client)
        self.assertEqual(audit['counts'], {'refreshed': 1, 'failed': 0, 'deferred': 0,
                                         'unsupported': 0, 'total': 1, 'attempted': 1})
        self.assertEqual(client.calls, [URL, BRIEF])
        self.assertNotEqual(before, after)
        self.assertNotIn('failure_stage', audit['results'][0])


if __name__ == '__main__':
    unittest.main()
