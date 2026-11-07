"""Unattended collection must fail closed and never fetch target assets."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import refresh_program_scopes as refresh

URL = 'https://bugcrowd.com/engagements/example'
PAGE = '{"getBriefVersionDocument":"/engagements/example/changelog/abc-123"}'
BODY = {'data': {'scope': [{'name': 'In scope', 'inScope': True,
                          'targets': [{'name': '*.example.com', 'category': 'website',
                                       'uri': 'https://example.com'}]}]}}
INTIGRITI_PAGE = '<lib-assets-detail><lib-asset-detail><div class="asset-name"><a href="https://example.com">example.com</a></div><lib-asset-type-label>URL</lib-asset-type-label><lib-bounty-tier-label>Out of scope</lib-bounty-tier-label></lib-asset-detail></lib-assets-detail>'

class RefreshTests(unittest.TestCase):
    def fresh(self, body=None):
        calls = []
        def get(url):
            calls.append(url)
            return json.dumps(BODY if body is None else body)
        result = refresh.parse_brief(URL, PAGE, get)
        self.assertEqual(calls, [URL + '/changelog/abc-123.json'])
        return result

    def test_exact_program_and_no_targets(self):
        fresh = self.fresh()
        self.assertEqual(fresh['assets'][0]['name'], '*.example.com')
        for url in ('http://bugcrowd.com/engagements/example', 'https://example.com',
                    URL + '?x=1', 'https://bugcrowd.com@evil.test/engagements/example'):
            with self.assertRaises(ValueError): refresh.official_url(url)
        with self.assertRaises(ValueError):
            refresh.parse_brief(URL, PAGE.replace('example', 'other'), lambda _: self.fail('Must not fetch'))

    def test_schema_drift_and_empty_table(self):
        for body in ({'data': {'scope': []}}, {'data': {'scope': [{}]}},
                     {'data': {'scope': [{'name': 'scope', 'inScope': 'true', 'targets': []}]}}):
            with self.assertRaises(ValueError): self.fresh(body)
        with self.assertRaises(ValueError):
            refresh.parse_brief(URL, 'login page', lambda _: self.fail('Must not fetch'))

    def test_bugcrowd_preserves_each_approved_origin_and_exact_identity(self):
        from scope_integrity import source_belongs_to_program
        for host in ('bugcrowd.com', 'www.bugcrowd.com', 'eu.bugcrowd.net', 'gov.bugcrowd.net'):
            url = 'https://' + host + '/engagements/example'
            get = Mock(return_value=json.dumps(BODY))
            with self.subTest(host=host):
                result = refresh.parse_brief(url, PAGE, get)
                source = url + '/changelog/abc-123.json'
                get.assert_called_once_with(source)
                self.assertEqual(result['source_url'], source)
                self.assertTrue(source_belongs_to_program('Bugcrowd', url, source, 'bugcrowd_scope'))
                self.assertEqual(refresh.official_url(source).netloc, host)
                for link in ('https://bugcrowd.com/engagements/example/changelog/abc-123',
                             '//bugcrowd.com/engagements/example/changelog/abc-123',
                             '/engagements/other/changelog/abc-123',
                             '/engagements/example/changelog/../abc-123',
                             '/engagements/example/changelog/abc-123?x=1'):
                    with self.subTest(link=link), self.assertRaises(ValueError):
                        refresh.parse_brief(url, json.dumps({'getBriefVersionDocument': link}),
                                            lambda _: self.fail('Must not fetch'))

    def test_bugcrowd_rejects_unapproved_origins_and_unsafe_forms_before_request(self):
        path = '/engagements/example'
        urls = ['https://' + host + path for host in
                ('bugcrowd.net', 'www.eu.bugcrowd.net', 'tracker.eu.bugcrowd.net',
                 'evil.bugcrowd.net', 'eu.bugcrowd.net.evil.test', 'eu.bugcrowd.net:443',
                 'user@eu.bugcrowd.net', 'eu.bugcrowd.net@evil.test')]
        urls += ['http://eu.bugcrowd.net' + path, 'https://gov.bugcrowd.net' + path + '?',
                 'https://eu.bugcrowd.net' + path + '#', ' https://eu.bugcrowd.net' + path,
                 'https://eu.bugcrowd.net\n' + path, 'https://eu.bugcrowd.net' + path + '\\child',
                 'https://eu.bugcrowd.net/engagements/example%2fchild',
                 'https://eu.bugcrowd.net/engagements/other/../example']
        client = refresh.PublicClient()
        client.opener = Mock()
        for url in urls:
            with self.subTest(url=url), patch.object(refresh.time, 'sleep') as sleep:
                with self.assertRaises(ValueError):
                    client.get(url)
                sleep.assert_not_called()
        client.opener.open.assert_not_called()

    def test_duplicate_rows_and_scope_direction(self):
        body = copy.deepcopy(BODY)
        body['data']['scope'][0]['targets'] *= 2
        body['data']['scope'].append(dict(body['data']['scope'][0], inScope=False))
        fresh = self.fresh(body)
        self.assertEqual(fresh['duplicate_source_rows'], 2)
        self.assertEqual(fresh['published_asset_count'], 4)
        updated = refresh.update_capture({'assets': []}, fresh)
        self.assertEqual(updated['published_asset_count'], len(updated['assets']) + updated['duplicate_source_rows'])
        self.assertEqual([x['scope'] for x in fresh['assets']], ['in', 'out'])

    def test_hackerone_csv_flags_and_exact_identity(self):
        header = 'identifier,asset_type,instruction,eligible_for_bounty,eligible_for_submission,availability_requirement,confidentiality_requirement,integrity_requirement,max_severity,system_tags,created_at,updated_at\n'
        body = header + 'example.com,URL,Restrictions apply,false,true,low,low,low,high,,2026-01-01,2026-01-01\n'
        calls = []
        def get(url):
            calls.append(url)
            return body
        result = refresh.parse_hackerone('https://hackerone.com/example?type=team', get)
        self.assertEqual(calls, ['https://hackerone.com/teams/example/assets/download_csv.csv'])
        self.assertEqual(result['assets'][0]['scope'], 'in')
        self.assertFalse(result['assets'][0]['bounty_eligible'])
        with self.assertRaises(ValueError): refresh.parse_hackerone('https://hackerone.com/example', lambda _: header)
        with self.assertRaises(ValueError): refresh.parse_hackerone('https://hackerone.com/example', lambda _: body.replace('false,true', 'false,unknown'))
        with self.assertRaises(ValueError): refresh.parse_hackerone('https://evil.test/example', get)

    def test_csv_provenance_is_exact_program_bound(self):
        from scope_integrity import source_belongs_to_program
        self.assertTrue(source_belongs_to_program('HackerOne', 'https://hackerone.com/example?type=team',
                        'https://hackerone.com/teams/example/assets/download_csv.csv', 'hackerone_scope'))
        self.assertFalse(source_belongs_to_program('HackerOne', 'https://hackerone.com/example',
                         'https://hackerone.com/teams/other/assets/download_csv.csv', 'hackerone_scope'))

    def test_intigriti_complete_table_and_tiers(self):
        source = '<lib-assets-detail><lib-asset-detail><div class="asset-name"><span></span><a href="https://example.com">example.com</a></div><lib-asset-type-label>URL</lib-asset-type-label><lib-bounty-tier-label>Out of scope</lib-bounty-tier-label></lib-asset-detail></lib-assets-detail>'
        url = 'https://app.intigriti.com/programs/example/program'
        result = refresh.parse_intigriti(url, lambda _: source)
        self.assertEqual(result['assets'][0]['scope'], 'out')
        self.assertEqual(result['assets'][0]['name'], 'example.com')
        self.assertEqual(result['source_url'], url + '/detail')
        for invalid in (source.replace('</lib-assets-detail>', ''), source.replace('</lib-asset-detail>', ''),
                        source.replace('Out of scope', 'Unknown'), source.replace('</lib-assets-detail>', '<button>Load more</button></lib-assets-detail>')):
            with self.assertRaises(ValueError): refresh.parse_intigriti(url, lambda _: invalid)

    def test_existing_intigriti_ampersand_path_round_trips_without_rewriting(self):
        base = 'https://app.intigriti.com/programs/uz%20leuven/ehealthhub&meta-hubvznkul'
        for url in (base, base + '/'):
            get = Mock(return_value=INTIGRITI_PAGE)
            with self.subTest(url=url):
                result = refresh.parse_intigriti(url, get)
                get.assert_called_once_with(base + '/detail')
                self.assertEqual(result['source_url'], base + '/detail')
                self.assertEqual(refresh.official_url(result['source_url']).netloc, 'app.intigriti.com')

    def test_intigriti_ampersand_exception_rejects_other_punctuation_and_unsafe_urls(self):
        base = 'https://app.intigriti.com/programs/uz%20leuven/ehealthhub&meta-hubvznkul'
        urls = [base + suffix for suffix in ('?', '#', '?x=1', '#scope', '//', '/detail', '/other')]
        urls += [base.replace('&', encoded) for encoded in ('%26', '%2526', '/', '%2f', '%3f', ';', '\\')]
        urls += [base.replace('uz%20leuven', 'other'), base.replace('meta-hubvznkul', 'other'),
                 base.replace('https:', 'http:'), base.replace('app.intigriti.com', 'app.intigriti.com.evil.test'),
                 base.replace('app.intigriti.com', 'user@app.intigriti.com'),
                 base.replace('app.intigriti.com', 'app.intigriti.com:443'),
                 base.replace('programs/', 'programs/other/../'), '\t' + base, base + '\n']
        for url in urls:
            with self.subTest(url=url):
                with self.assertRaises(ValueError):
                    refresh.parse_intigriti(url, lambda _: self.fail('Must not fetch'))
                with self.assertRaises(ValueError):
                    refresh.official_url(url + '/detail')

    def test_display_url_alias_deduplication(self):
        self.assertEqual(refresh.queue_identity({'platform': 'HackerOne', 'program_url': 'https://hackerone.com/example?type=team'}), 'https://hackerone.com/example')

    def test_removal_guard(self):
        with self.assertRaises(ValueError):
            refresh.protect_removals([{'name': 'old', 'scope': 'in'}], self.fresh()['assets'])

    def test_capture_preserves_directory_metadata(self):
        record = {'program_url': URL, 'platform': 'Bugcrowd', 'assets': [], 'captured_at': 'old',
                  'listing_id': 'stable', 'gap_review': {}, 'error': 'old'}
        result = refresh.update_capture(record, self.fresh())
        self.assertEqual(result['listing_id'], 'stable')
        self.assertNotIn('gap_review', result)
        self.assertEqual(record['captured_at'], 'old')

    def test_policy_only_advances_scope_evidence(self):
        record = {'last_verified_at': 'old-policy', 'eligibility': {'source_ids': ['policy']},
                  'sources': [{'id': 'policy'}, {'id': 'old-assets'}],
                  'asset_scope': {'source_ids': ['old-assets'], 'in_scope': [], 'out_of_scope': []}}
        result = refresh.update_program(record, self.fresh())
        self.assertEqual(result['last_verified_at'], 'old-policy')
        self.assertEqual(result['eligibility'], record['eligibility'])
        self.assertNotIn('old-assets', [s['id'] for s in result['sources']])
        self.assertIn('policy', [s['id'] for s in result['sources']])

    def test_failed_fetch_retains_last_good_and_audits_all(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'data/programs').mkdir(parents=True)
            rows = [{'program_url': URL + str(i), 'platform': 'Bugcrowd', 'assets': [],
                     'captured_at': 'old'} for i in range(3)]
            rows.append({'program_url': 'https://example.com/security', 'platform': 'Independent', 'assets': []})
            for path, captures in zip(refresh.CAPTURES, [rows, []]):
                refresh.dump(root / path, {'captures': captures})
            class Client:
                def get(self, url): raise HTTPError(url, 429, 'Too many requests', {}, None)
            audit = refresh.refresh(root, Client())
            self.assertEqual(audit['counts'], {'refreshed': 0, 'failed': 1, 'deferred': 2,
                                             'unsupported': 1, 'total': 4, 'attempted': 1})
            self.assertEqual(json.loads((root / refresh.CAPTURES[0]).read_text())['captures'], rows)
            self.assertTrue(audit['completed_at'])

if __name__ == '__main__': unittest.main()
