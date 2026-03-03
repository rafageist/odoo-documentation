---
tags: [odoo, enterprise, generated, views]
---

# data/account_return_check_template.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `data/account_return_check_template.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `account_return_check_template_non_recoverable_vat_gross_accounting_view`
- Name: account.move.line.list
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `tax_ids`
- XPath or positional patches: 0

## Actions

- `account_return_check_template_non_recoverable_vat_gross_accounting_action`: `act_window` Journal Items

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

