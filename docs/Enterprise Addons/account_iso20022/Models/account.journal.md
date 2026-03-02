<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.journal

- Module: [[docs/Enterprise Addons/account_iso20022/account_iso20022|account_iso20022]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_journal.py`, `models/account_journal_dashboard.py`, `models/account_journal_iso20022_ch.py`, `models/account_journal_iso20022_se.py`, `models/account_journal_iso20022_us.py`, `models/account_journal_sepa_ct.py`, and 2 more
- Python classes: `AccountJournal`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 2, `Selection` x 3
- Relation fields: 0

## Sample fields

- `has_iso20022_payment_method`: `Boolean` (compute `_compute_has_iso20022_payment_method`)
- `has_sepa_ct_payment_method`: `Boolean` (compute `_compute_has_sepa_ct_payment_method`)
- `iso20022_charge_bearer`: `Selection`
- `iso20022_default_priority`: `Selection`
- `sepa_pain_version`: `Selection` (compute `_compute_sepa_pain_version`, store `True`)

## Method hints

- Detected methods: 37
- Action methods: `action_sepa_ct_to_send`
- Compute methods: `_compute_has_iso20022_payment_method`, `_compute_has_sepa_ct_payment_method`, `_compute_sepa_pain_version`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_iso20022/Models]]

<!-- GENERATED:MODEL -->
