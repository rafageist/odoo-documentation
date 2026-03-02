<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/invoice_report_view.xml

- Module: [[docs/Community Addons/l10n_ar/l10n_ar|l10n_ar]]
- Scope: Community Addons
- Source file: `report/invoice_report_view.xml`
- Views: 1
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `view_account_invoice_report_search_inherit`
- Name: account.invoice.report.search
- Model: `account.invoice.report`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_report_search`
- Root tag: `search`
- Field references: 1
- Sample fields: `l10n_ar_state_id`
- XPath or positional patches: 1

## Actions

- `action_iibb_purchases_by_state_and_account_pivot`: `act_window` IIBB - Purchases by jurisdiction
- `action_iibb_sales_by_state_and_account_pivot`: `act_window` IIBB - Sales by jurisdiction

## Menus

- `menu_iibb_purchases_by_state_and_account`: unnamed
- `menu_iibb_sales_by_state_and_account`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ar/Views]]

<!-- GENERATED:VIEWFILE -->
