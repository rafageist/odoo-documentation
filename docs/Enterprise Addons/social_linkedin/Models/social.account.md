<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.account

- Module: [[docs/Enterprise Addons/social_linkedin/social_linkedin|social_linkedin]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_account.py`
- Python classes: `SocialAccount`

## Field footprint

- Detected fields: 3
- Field types: `Char` x 3
- Relation fields: 0

## Sample fields

- `linkedin_access_token`: `Char` (comodel `LinkedIn access token`)
- `linkedin_account_id`: `Char` (comodel `LinkedIn Account ID`, compute `_compute_linkedin_account_id`)
- `linkedin_account_urn`: `Char` (comodel `LinkedIn Account URN`)

## Method hints

- Detected methods: 13
- Action methods: none
- Compute methods: `_compute_linkedin_account_id`, `_compute_statistics`, `_compute_statistics_linkedin`, `_compute_stats_link`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_linkedin/Models]]

<!-- GENERATED:MODEL -->
