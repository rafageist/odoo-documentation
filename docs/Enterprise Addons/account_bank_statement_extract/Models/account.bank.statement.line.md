<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.bank.statement.line

- Module: [[docs/Enterprise Addons/account_bank_statement_extract/account_bank_statement_extract|account_bank_statement_extract]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_bank_statement_line.py`
- Python classes: `AccountBankStatementLine`

## Field footprint

- Detected fields: 2
- Field types: `Monetary` x 2
- Relation fields: 0

## Sample fields

- `credit`: `Monetary` (compute `_compute_debit_credit`)
- `debit`: `Monetary` (compute `_compute_debit_credit`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_debit_credit`
- Onchange methods: `_inverse_credit`, `_inverse_debit`

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_bank_statement_extract/Models]]

<!-- GENERATED:MODEL -->
