<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.thread.phone

- Module: [[docs/Community Addons/phone_validation/phone_validation|phone_validation]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mail_thread_phone.py`
- Python classes: `MailThreadPhone`
- Description: Phone Blacklist Mixin
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 2, `Char` x 2
- Relation fields: 0

## Sample fields

- `phone_blacklisted`: `Boolean` (compute `_compute_blacklisted`, store `False`)
- `phone_mobile_search`: `Char` (comodel `Phone Number`, store `False`)
- `phone_sanitized`: `Char` (compute `_compute_phone_sanitized`, store `True`)
- `phone_sanitized_blacklisted`: `Boolean` (compute `_compute_blacklisted`, store `False`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_blacklisted`, `_compute_phone_sanitized`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/phone_validation/Models]]

<!-- GENERATED:MODEL -->
