<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/account_invoice_report_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `report/account_invoice_report_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `account_invoice_report_view_tree`
- Name: account.invoice.report.view.list.inherit.sale
- Model: `account.invoice.report`
- Type: inferred from arch
- Inherits: `account.account_invoice_report_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `invoice_user_id`, `team_id`
- XPath or positional patches: 0

### `view_account_invoice_report_search_inherit`
- Name: account.invoice.report.search.inherit
- Model: `account.invoice.report`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_report_search`
- Root tag: `filter`
- Field references: 2
- Sample fields: `invoice_user_id`, `team_id`
- XPath or positional patches: 1

## Actions

- `action_account_invoice_report_salesteam`: `act_window` Invoices Analysis

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

<!-- GENERATED:VIEWFILE -->
