import copy
import datetime as dt
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from discover_programs import build_report


class DiscoveryImportTests(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 11, 7, 12, tzinfo=dt.timezone.utc)
        self.baseline = {'listings': [{'platform': 'HackerOne', 'program_url': 'https://hackerone.com/known'}]}
        self.page = {'number': 1, 'url': 'https://hackerone.com/directory/programs',
                     'observed_at': '2026-11-07T11:00:00Z', 'advertised_total': 2,
                     'pagination_exhausted': True, 'entries': [
                         {'name': 'Known', 'program_url': 'https://hackerone.com/known?type=team'},
                         {'name': 'New', 'program_url': 'https://hackerone.com/new'}]}
        self.capture = {'platform': 'HackerOne', 'filters': 'Active; launch descending', 'pages': [self.page]}

    def report(self):
        return build_report(self.baseline, {'platforms': [self.capture]}, self.now)

    def result(self):
        return self.report()['platforms'][1]

    def test_missing_is_unknown_not_zero(self):
        r = build_report(self.baseline, now=self.now)
        self.assertIsNone(r['counts']['new_programs'])
        self.assertTrue(all(p['status'] == 'needs_browser' for p in r['platforms']))

    def test_canonical_dedup_and_partial_coverage(self):
        self.assertEqual(self.result()['new_count'], 1)
        self.assertEqual(self.result()['candidates'][0]['submission_status'], 'unknown')
        self.assertIsNone(self.report()['counts']['new_programs'])
        self.assertEqual(self.report()['counts']['validated_candidates'], 1)

    def test_no_baseline_mutation(self):
        original = copy.deepcopy(self.baseline)
        self.report()
        self.assertEqual(self.baseline, original)

    def test_invalid_observation_variants(self):
        mutations = [lambda p: p.update(number=2), lambda p: p.update(pagination_exhausted=False),
                     lambda p: p.update(entries=[]), lambda p: p.update(advertised_total=3),
                     lambda p: p.update(observed_at='2020-01-01T00:00:00Z'),
                     lambda p: p.update(observed_at='2027-01-01T00:00:00Z'),
                     lambda p: p.update(url='https://example.com/directory'),
                     lambda p: p['entries'][1].update(program_url='https://hackerone.com/known/'),
                     lambda p: p['entries'][1].update(program_url='https://evil.test/new'),
                     lambda p: p['entries'][1].update(program_url='https://user@hackerone.com/new'),
                     lambda p: p['entries'][1].update(program_type='confirmed_eligible')]
        original = copy.deepcopy(self.page)
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                self.capture['pages'] = [copy.deepcopy(original)]
                mutation(self.capture['pages'][0])
                self.assertEqual(self.result()['status'], 'invalid_observation')
                self.assertIsNone(self.result()['new_count'])

    def test_multiple_pages(self):
        second = copy.deepcopy(self.page)
        second.update(number=2, entries=[second['entries'][1]])
        self.page.update(pagination_exhausted=False, entries=[self.page['entries'][0]])
        self.capture['pages'].append(second)
        self.assertEqual(self.result()['observed_count'], 2)
        second['advertised_total'] = 3
        self.assertEqual(self.result()['status'], 'invalid_observation')

    def test_unknown_total_requires_exhaustion(self):
        self.page['advertised_total'] = None
        self.assertEqual(self.result()['status'], 'complete_visible_listing')
        self.page['pagination_exhausted'] = False
        self.assertEqual(self.result()['status'], 'invalid_observation')

    def test_duplicate_platform_rejected(self):
        with self.assertRaises(ValueError):
            build_report(self.baseline, {'platforms': [self.capture, self.capture]}, self.now)


if __name__ == '__main__':
    unittest.main()
