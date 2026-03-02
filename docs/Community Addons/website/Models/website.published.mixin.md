<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# website.published.mixin

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mixins.py`
- Python classes: `WebsitePublishedMixin`
- Description: Website Published Mixin

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 3, `Char` x 2
- Relation fields: 0

## Sample fields

- `can_publish`: `Boolean` (comodel `Can Publish`, compute `_compute_can_publish`)
- `is_published`: `Boolean` (comodel `Is Published`)
- `website_absolute_url`: `Char` (comodel `Website Absolute URL`, compute `_compute_website_absolute_url`)
- `website_published`: `Boolean` (comodel `Visible on current website`, related `is_published`)
- `website_url`: `Char` (comodel `Website URL`, compute `_compute_website_url`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_can_publish`, `_compute_website_absolute_url`, `_compute_website_url`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/website/Models]]

<!-- GENERATED:MODEL -->
