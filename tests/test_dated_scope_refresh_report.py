"""Keep the November 7 refresh report's gaps explicit and historically dated."""

from collections import Counter
import json
from pathlib import Path
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


class DatedScopeRefreshReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / 'exports/scope-refresh-2026-11-07.json').read_text())
        cls.page = (ROOT / 'docs/scope-refresh-2026-11-07.md').read_text()
        cls.failures = cls.report['failed_or_unavailable_sources']

    def test_failure_sources_have_nonempty_unique_https_urls(self):
        urls = []
        for failure in self.failures:
            with self.subTest(failure=failure):
                url = failure['url']
                self.assertIsInstance(url, str)
                parsed = urlsplit(url)
                self.assertEqual(parsed.scheme, 'https')
                self.assertTrue(parsed.netloc)
                self.assertFalse(parsed.fragment)
                self.assertTrue(failure['reason'].strip())
                urls.append(url)
        self.assertEqual(len(urls), len(set(urls)))

    def test_report_and_page_retain_every_failure(self):
        self.assertNotIn('(None)', self.page)
        for failure in self.failures:
            self.assertIn(
                f"- [{failure['platform']} source]({failure['url']}): {failure['reason']}",
                self.page)

    def test_adobe_identity_is_restored_without_inventing_gate_reason(self):
        adobe = [failure for failure in self.failures if failure['url'] ==
                 'https://app.intigriti.com/programs/adobe/adobepublic']
        self.assertEqual(len(adobe), 1)
        self.assertEqual(adobe[0]['platform'], 'Intigriti')
        self.assertIn('destination was not recorded', adobe[0]['reason'])
        self.assertIn('no gate classification is inferred', adobe[0]['reason'])
        self.assertIn('Prior scope and verification date retained.', adobe[0]['reason'])

    def test_gate_explanations_distinguish_historical_review_from_refresh(self):
        failures = [failure for failure in self.failures if failure['platform'] == 'Intigriti']
        self.assertEqual(len(failures), 31)
        kinds = Counter()
        for failure in failures:
            reason = failure['reason']
            self.assertTrue(reason.startswith('HTTP 302 on 2026-11-07.'))
            for kind in ('preview/login gate', 'terms/login gate'):
                if kind in reason:
                    kinds[kind] += 1
                    self.assertIn('last detailed access review (2026-10-03)', reason)
                    self.assertIn('did not traverse the redirect or verify a scope table', reason)
        self.assertEqual(kinds, {'preview/login gate': 18, 'terms/login gate': 12})

    def test_historical_coverage_totals_are_unchanged(self):
        self.assertEqual(self.report['review_date'], '2026-11-07')
        self.assertEqual(self.report['canonical_records_refreshed'], 823)
        self.assertEqual(self.report['records_with_scope_row_changes'], 105)
        gaps = Counter(failure['platform'] for failure in self.failures)
        self.assertEqual(gaps, {'Bugcrowd': 11, 'HackerOne': 1, 'Intigriti': 31, 'Direct policy': 1})
        for coverage in self.report['coverage']:
            self.assertEqual(coverage['official_program_sources_attempted'] - coverage['freshly_read'],
                             gaps[coverage['platform']])

    def test_supplemental_policy_context_is_not_platform_verification(self):
        self.assertIn('## Supplemental policy evidence reviewed November 7, 2026', self.page)
        self.assertIn('They do not recover the missing platform tables', self.page)
        self.assertIn('Both retained platform rows already have scope=out.', self.page)
        self.assertIn('No scope row was changed in this review.', self.page)
        self.assertIn('https://www.oshrc.gov/vulnerability-disclosure-policy/', self.page)


if __name__ == '__main__':
    unittest.main()
