<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.thread.blacklist

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mail_thread_blacklist.py`
- Python classes: `MailThreadBlacklist`
- Description: Mail Blacklist mixin
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 1, `Integer` x 1
- Relation fields: 0

## Sample fields

- `email_normalized`: `Char` (compute `_compute_email_normalized`, store `True`)
- `is_blacklisted`: `Boolean` (compute `_compute_is_blacklisted`, store `False`)
- `message_bounce`: `Integer` (comodel `Bounce`)

## Method hints

- Detected methods: 8
- Action methods: none
- Compute methods: `_compute_email_normalized`, `_compute_is_blacklisted`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/mail/Models]]

<!-- GENERATED:MODEL -->
