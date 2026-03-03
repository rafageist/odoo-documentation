<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/account_invoice_report_view.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `report/account_invoice_report_view.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_report_search`
- Name: account.invoice.report.search
- Model: `account.invoice.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `invoice_date`, `invoice_user_id`, `partner_id`, `product_categ_id`, `product_id`
- XPath or positional patches: 0

### `account_invoice_report_view_tree`
- Name: account.invoice.report.view.list
- Model: `account.invoice.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 21
- Sample fields: `company_id`, `country_id`, `inventory_value`, `invoice_date`, `invoice_date_due`, `invoice_user_id`, `journal_id`, `move_id`, `move_type`, `partner_id`, and 11 more
- XPath or positional patches: 0

### `view_account_invoice_report_graph`
- Name: account.invoice.report.graph
- Model: `account.invoice.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `price_subtotal`, `product_categ_id`
- XPath or positional patches: 0

### `view_account_invoice_report_pivot`
- Name: account.invoice.report.pivot
- Model: `account.invoice.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `invoice_date`, `price_subtotal`, `product_categ_id`
- XPath or positional patches: 0

## Actions

- `action_account_invoice_report_all`: `act_window` Invoices Analysis
- `action_account_invoice_report_all_supp`: `act_window` Bills Analysis

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
