<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.job

- Module: [[docs/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/hr_job.py`
- Python classes: `HrJob`
- Inherits: `website.published.multi.mixin`, `website.searchable.mixin`, `website.seo.metadata`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 1, `Date` x 1, `Html` x 3
- Relation fields: 0

## Sample fields

- `description`: `Html` (comodel `Job Description`)
- `full_url`: `Char` (comodel `job URL`, compute `_compute_full_url`)
- `job_details`: `Html` (comodel `Process Details`)
- `published_date`: `Date` (compute `_compute_published_date`, store `True`)
- `website_description`: `Html` (comodel `Website description`)
- `website_published`: `Boolean`

## Method hints

- Detected methods: 10
- Action methods: `action_archive`
- Compute methods: `_compute_full_url`, `_compute_published_date`, `_compute_website_url`
- Onchange methods: `_onchange_website_published`

## Navigation

- **Parent:** [[docs/Community Addons/website_hr_recruitment/Models]]

<!-- GENERATED:MODEL -->
