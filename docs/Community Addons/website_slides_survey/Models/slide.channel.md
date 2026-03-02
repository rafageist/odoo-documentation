<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# slide.channel

- Module: [[docs/Community Addons/website_slides_survey/website_slides_survey|website_slides_survey]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/slide_channel.py`
- Python classes: `SlideChannel`

## Field footprint

- Detected fields: 2
- Field types: `Integer` x 2
- Relation fields: 0

## Sample fields

- `members_certified_count`: `Integer` (comodel `# Certified Attendees`, compute `_compute_members_certified_count`)
- `nbr_certification`: `Integer` (comodel `Number of Certifications`, compute `_compute_slides_statistics`, store `True`)

## Method hints

- Detected methods: 3
- Action methods: `action_redirect_to_certified_members`
- Compute methods: `_compute_members_certified_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/website_slides_survey/Models]]

<!-- GENERATED:MODEL -->
