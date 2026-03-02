<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.test.ticket.el

- Module: [[docs/Community Addons/test_mail/test_mail|test_mail]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mail_test_ticket.py`
- Python classes: `MailTestTicketEl`
- Description: Ticket-like model with exclusion list
- Inherits: `mail.test.ticket`, `mail.thread.blacklist`

## Field footprint

- Detected fields: 1
- Field types: `Char` x 1
- Relation fields: 0

## Sample fields

- `email_from`: `Char` (comodel `Email`, compute `_compute_email_from`, store `True`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_email_from`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/test_mail/Models]]

<!-- GENERATED:MODEL -->
