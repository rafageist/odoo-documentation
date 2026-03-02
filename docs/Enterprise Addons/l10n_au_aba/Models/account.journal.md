<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.journal

- Module: [[docs/Enterprise Addons/l10n_au_aba/l10n_au_aba|l10n_au_aba]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_journal.py`, `models/account_journal_dashboard.py`
- Python classes: `AccountJournal`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Char` x 4
- Relation fields: 0

## Sample fields

- `aba_bsb`: `Char` (related `bank_account_id.aba_bsb`)
- `aba_fic`: `Char`
- `aba_self_balancing`: `Boolean`
- `aba_user_number`: `Char`
- `aba_user_spec`: `Char`

## Method hints

- Detected methods: 6
- Action methods: `action_aba_ct_to_send`
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_aba/Models]]

<!-- GENERATED:MODEL -->
