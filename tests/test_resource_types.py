"""Offline regression coverage for primary-publication resource classification."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_navigation import resource_pages
from export_resources import build_export
from validate import Invalid
from validate_extra import validate_all, validate_resource

# Reviewed migration examples, not a classifier or an exhaustive future inventory.
MIGRATED_IDS = ('angular-2026-host-binding-context-authority',
 'angular-2026-raw-content-serialization-context',
 'astro-2026-route-normalization-authorization-consistency',
 'axios-2026-streamed-upload-budget-enforcement',
 'better-auth-2026-authorization-code-consumption-integrity',
 'better-auth-2026-local-account-linking-verification',
 'bugsink-2026-token-expiry-unit-integrity',
 'coder-2026-provisioned-object-ownership-integrity',
 'directus-2026-preauthorization-side-effect-integrity',
 'django-2026-query-alias-structure-boundary',
 'filebrowser-2026-share-owner-permission-lifecycle',
 'grav-2026-session-account-state-revalidation',
 'hotcrp-2026-contact-authorship-permission-boundary',
 'langflow-2026-mcp-resource-project-authorization',
 'librechat-2026-mcp-oauth-session-binding',
 'mailcow-2026-persisted-data-query-boundary',
 'n8n-2026-dynamic-credential-object-authority',
 'n8n-2026-ldap-account-linking-authority',
 'n8n-2026-refresh-grant-resource-binding',
 'nhost-2026-provider-claim-verification-provenance',
 'nuxt-2026-rendered-payload-cache-authorization',
 'obot-2026-oauth-audience-and-consent-boundaries',
 'open-webui-2026-connection-credential-capture',
 'open-webui-2026-realtime-revocation-consistency',
 'open-webui-2026-role-claim-provenance-and-revocation',
 'outline-2026-webhook-revocation-lifecycle',
 'parse-server-2026-upload-metadata-consumer-boundary',
 'paymenter-2026-refund-transition-atomicity',
 'prowler-2026-saml-tenant-issuance-binding',
 'pterodactyl-2026-delegated-token-purpose-binding',
 'pypdf-2026-attachment-processing-cost-boundary',
 'qwik-2026-resumability-comment-serialization-boundary',
 'react-router-2026-hydration-error-constructor-boundary',
 'serialize-javascript-2026-output-code-boundary',
 'steeltoe-2026-diagnostic-uri-data-minimization',
 'sylius-2026-payment-action-authority',
 'typo3-2026-upload-validator-lifecycle-boundary',
 'vikunja-2026-favorites-current-access-revalidation',
 'vvveb-2026-order-domain-invariant')

RESEARCH_IDS = (
    'sveltekit-2026-origin-routing-trust-boundary',
    'frappe-2026-linked-document-response-authorization',
    'portswigger-2025-upstream-http-framing-boundaries',
    'arxiv-2026-cache-key-precision-and-capacity',
)


class ResourceTypeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resources, cls.diagrams, cls.taxonomy = validate_all()
        cls.records = {r['id']: r for r in cls.resources}
        cls.skills = json.loads((ROOT / 'data/taxonomy.json').read_text())
        cls.schema = json.loads((ROOT / 'schema/resource.schema.json').read_text())

    def test_taxonomy_retains_existing_types_and_adds_one_advisory_id(self):
        expected = {
            'security-standard': 'Security Standard',
            'technical-standard': 'Technical Standard',
            'implementation-guide': 'Implementation Guide',
            'architecture-guide': 'Architecture Guide',
            'reporting-guide': 'Reporting Guide',
            'training-lab': 'Training Lab',
            'research-paper': 'Research Paper',
            'maintainer-advisory': 'Maintainer Advisory',
        }
        types = self.taxonomy['resource_types']
        self.assertEqual(len(types), len({t['id'] for t in types}))
        actual = {t['id']: t['title'] for t in types}
        for key, title in expected.items():
            self.assertEqual(actual[key], title)

    def test_reviewed_maintainer_publications_are_classified(self):
        for rid in MIGRATED_IDS:
            with self.subTest(resource=rid):
                self.assertEqual(self.records[rid]['resource_type_id'], 'maintainer-advisory')

    def test_research_is_not_reclassified_by_corroborating_advisories(self):
        for rid in RESEARCH_IDS:
            with self.subTest(resource=rid):
                self.assertEqual(self.records[rid]['resource_type_id'], 'research-paper')

    def test_validation_accepts_taxonomy_member_and_rejects_unknown_type(self):
        rec = copy.deepcopy(self.records[MIGRATED_IDS[0]])
        skills = {s['id'] for s in self.skills['skillsets']}
        validate_resource(rec, self.schema, self.taxonomy, skills)
        rec['resource_type_id'] = 'unknown-resource-type'
        with self.assertRaisesRegex(Invalid, 'unknown resource type'):
            validate_resource(rec, self.schema, self.taxonomy, skills)

    def test_export_preserves_canonical_records_and_taxonomy(self):
        exported = build_export()
        self.assertEqual(exported['taxonomy'], self.taxonomy)
        self.assertEqual({r['id']: r for r in exported['resources']}, self.records)
        self.assertEqual(exported['counts']['resources'], len(self.records))
        self.assertEqual(exported, build_export())

    def test_readable_pages_and_index_follow_taxonomy_labels(self):
        pages = resource_pages(self.resources, self.diagrams, self.taxonomy, self.skills)
        index = pages['docs/resource-index.md']
        for ids, label in ((MIGRATED_IDS, 'Maintainer Advisory'), (RESEARCH_IDS, 'Research Paper')):
            for rid in ids:
                with self.subTest(resource=rid):
                    self.assertIn('**Resource type:** ' + label, pages['docs/resources/' + rid + '.md'])
                    entry = next(line for line in index.splitlines() if 'resources/' + rid + '.md' in line)
                    self.assertIn('; ' + label + '.', entry)


if __name__ == '__main__':
    unittest.main()
