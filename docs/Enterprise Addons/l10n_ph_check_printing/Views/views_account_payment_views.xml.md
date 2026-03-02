<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_payment_views.xml

- Module: [[docs/Enterprise Addons/l10n_ph_check_printing/l10n_ph_check_printing|l10n_ph_check_printing]]
- Scope: Enterprise Addons
- Source file: `views/account_payment_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_account_payment_check_warehouse_search`
- Name: account.payment.check.warehouse.search
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_account_supplier_payment_check_warehouse_tree`
- Name: account.supplier.payment.check.warehouse.list
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `list`
- Field references: 4
- Sample fields: `check_number`, `date`, `is_matched`, `partner_id`
- XPath or positional patches: 1

## Actions

- `action_account_payments_payable_check_warehouse`: `act_window` Check Warehouse

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ph_check_printing/Views]]

<!-- GENERATED:VIEWFILE -->
