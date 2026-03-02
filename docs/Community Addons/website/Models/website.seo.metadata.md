<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# website.seo.metadata

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mixins.py`
- Python classes: `WebsiteSeoMetadata`
- Description: SEO metadata

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 4, `Text` x 1
- Relation fields: 0

## Sample fields

- `is_seo_optimized`: `Boolean` (comodel `SEO optimized`, compute `_compute_is_seo_optimized`, store `True`)
- `seo_name`: `Char` (comodel `Seo name`)
- `website_meta_description`: `Text` (comodel `Website meta description`)
- `website_meta_keywords`: `Char` (comodel `Website meta keywords`)
- `website_meta_og_img`: `Char` (comodel `Website opengraph image`)
- `website_meta_title`: `Char` (comodel `Website meta title`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_is_seo_optimized`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/website/Models]]

<!-- GENERATED:MODEL -->
