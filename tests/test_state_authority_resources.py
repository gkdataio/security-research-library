"""Offline editorial guardrails for restored state and confirmation authority."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_navigation import build
from export_resources import build_export
from validate import validate_library
from validate_extra import validate_all
from vulnerability_navigation import selected_memberships


class StateAuthorityResourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resources, _, _ = validate_all()
        cls.records = {record['id']: record for record in cls.resources}
        cls.reports, _ = validate_library()
        cls.config = json.loads((ROOT / 'data/vulnerability-navigation.json').read_text())
        cls.pages = build()
        cls.angular_id = 'angular-2026-hydration-state-source-authenticity'
        cls.saleor_id = 'saleor-2026-email-change-confirmation-binding'

    def test_advisories_keep_original_publications_and_unknown_editions(self):
        expected = {
            self.angular_id: ('2026-06-10', 'angular/angular', 'GHSA-rgjc-h3x7-9mwg'),
            self.saleor_id: ('2026-04-08', 'saleor/saleor', 'GHSA-hwph-9537-mc3p'),
        }
        for rid, (date, repo, advisory) in expected.items():
            with self.subTest(resource=rid):
                record = self.records[rid]
                self.assertEqual(record['resource_type_id'], 'maintainer-advisory')
                self.assertEqual(record['authors'], [])
                self.assertIsNone(record['version'])
                self.assertIsNone(record['dates']['version_released']['value'])
                self.assertEqual(record['primary_url'],
                                 f'https://github.com/{repo}/security/advisories/{advisory}')
                for field in ('published', 'source_displayed'):
                    self.assertEqual(record['dates'][field]['value'], date)
                    self.assertEqual(record['dates'][field]['source_id'], 'advisory')
                    self.assertEqual(record['dates'][field]['basis'], 'explicit')

    def test_angular_retains_applicability_and_conditional_impact(self):
        record = self.records[self.angular_id]
        for phrase in ('SSR with hydration', 'untrusted influence',
                       'XSS depends on unsafe downstream rendering', 'parseable data'):
            self.assertIn(phrase, record['summary'])
        caveats = ' '.join(record['caveats'])
        for phrase in ('22.0.1', '21.2.17', '20.3.25', '<= 19.2.25',
                       'no listed patch', 'does not establish production compromise'):
            self.assertIn(phrase, caveats)
        self.assertEqual(record['topic_ids'], ['web-foundations'])
        self.assertEqual(set(record['skillset_ids']), {
            'untrusted-input-handling', 'cache-artifact-isolation', 'patch-verification'})

    def test_angular_has_only_source_explicit_parent_xss_membership(self):
        members = [m for m in self.config['memberships'] if m['record_id'] == self.angular_id]
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0]['type_id'], 'xss')
        self.assertEqual(members[0]['basis'], 'source_explicit')
        self.assertEqual(members[0]['source_ids'], ['advisory'])
        self.assertIn('conditional on unsafe downstream rendering', members[0]['rationale'])
        for subtype in ('stored-xss', 'reflected-xss', 'blind-xss'):
            entries = selected_memberships(subtype, self.config, self.reports, self.resources)
            self.assertNotIn(self.angular_id, {entry['record']['id'] for entry in entries})
            self.assertNotIn(self.angular_id, self.pages[f'docs/vulnerabilities/{subtype}.md'])

    def test_angular_development_and_database_dates_stay_separate(self):
        record = self.records[self.angular_id]
        caveats = ' '.join(record['caveats'])
        for phrase in ('opened June 1 and merged June 3, 2026',
                       'publication there on June 15', 'update on July 15, 2026',
                       'Software-release dates were not established'):
            self.assertIn(phrase, caveats)
        sources = {source['id']: source for source in record['sources']}
        self.assertEqual(sources['patch']['url'], 'https://github.com/angular/angular/pull/69064')
        self.assertEqual(sources['advisory-database']['supports'], ['dates'])

    def test_saleor_retains_authenticated_access_and_branch_context(self):
        record = self.records[self.saleor_id]
        self.assertIn('valid confirmation token for one account and authenticated access to a second account',
                      record['summary'])
        self.assertIn('not an unauthenticated takeover claim', record['summary'])
        caveats = ' '.join(record['caveats'])
        for phrase in ('3.23.0a3', '3.22.47', '3.21.54', '3.20.118',
                       'each start at 2.10.0', '3.23.0a3 is a prerelease',
                       'no known workaround', 'maintainer-described potential impact',
                       'do not establish a controlled independent demonstration or a production incident'):
            self.assertIn(phrase, caveats)
        self.assertEqual(set(record['topic_ids']), {'identity', 'authorization', 'business-logic'})
        self.assertEqual(set(record['skillset_ids']), {
            'authorization-modeling', 'security-token-design',
            'identity-lifecycle-review', 'patch-verification'})

    def test_saleor_patch_scope_and_execution_limits_are_explicit(self):
        record = self.records[self.saleor_id]
        for phrase in ('one subject, one operation', 'expected current state',
                       'prior email state', 'does not establish a successful test run'):
            self.assertIn(phrase, record['defensive_use'])
        self.assertIn('Upstream code was not executed', record['freshness']['note'])
        caveats = ' '.join(record['caveats'])
        self.assertIn('bundles other security changes', caveats)
        self.assertIn('Commit and software-release dates were not established', caveats)
        sources = {source['id']: source for source in record['sources']}
        self.assertEqual(sources['patch']['url'],
                         'https://github.com/saleor/saleor/commit/f0371bdd4cafcc841f1a9e7049cead6133bf7464')
        self.assertEqual(sources['patch']['supports'], ['summary'])
        self.assertEqual(sources['patch-tests']['supports'], ['summary'])

    def test_credits_do_not_become_authors_or_awards(self):
        angular = ' '.join(self.records[self.angular_id]['caveats'])
        saleor = ' '.join(self.records[self.saleor_id]['caveats'])
        for phrase in ('SkyZeroZx is credited as Reporter', 'alan-agius4 published',
                       'AndrewKushnir and JeanMeche', 'josephperrott is credited as Other'):
            self.assertIn(phrase, angular)
        self.assertIn('NyanKiyoshi published', saleor)
        self.assertIn('ch1nhpd is credited as Reporter', saleor)
        reports = {report['id'] for report in self.reports}
        for rid in (self.angular_id, self.saleor_id):
            self.assertNotIn(rid, reports)
            self.assertNotIn('reward', self.records[rid])
            self.assertEqual(self.records[rid]['prerequisites_basis'], 'editorial_guidance')

    def test_export_and_readable_routes_preserve_both_records_once(self):
        exported = build_export()['resources']
        for rid in (self.angular_id, self.saleor_id):
            matches = [record for record in exported if record['id'] == rid]
            self.assertEqual(matches, [self.records[rid]])
            self.assertEqual(self.pages['docs/resource-index.md'].count(f'(<resources/{rid}.md>)'), 1)
            self.assertEqual(self.pages['docs/resource-topics.md'].count(f'(<resources/{rid}.md>)'),
                             len(self.records[rid]['topic_ids']))
            self.assertEqual((ROOT / f'docs/resources/{rid}.md').read_text(),
                             self.pages[f'docs/resources/{rid}.md'])
        self.assertIn(self.angular_id, self.pages['docs/vulnerabilities/xss.md'])
        for category in ('authentication', 'authorization', 'business-logic'):
            self.assertIn(self.saleor_id, self.pages[f'docs/categories/{category}.md'])


if __name__ == '__main__':
    unittest.main()
