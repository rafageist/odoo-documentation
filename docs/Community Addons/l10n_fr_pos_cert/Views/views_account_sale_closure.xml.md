<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_sale_closure.xml

- Module: [[docs/Community Addons/l10n_fr_pos_cert/l10n_fr_pos_cert|l10n_fr_pos_cert]]
- Scope: Community Addons
- Source file: `views/account_sale_closure.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `form_view_account_sale_closing`
- Name: Sales Closings
- Model: `account.sale.closing`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `company_id`, `cumulative_total`, `currency_id`, `date_closing_start`, `date_closing_stop`, `frequency`, `last_order_hash`, `last_order_id`, `name`, `sequence_number`, and 1 more
- XPath or positional patches: 0

### `list_view_account_sale_closing`
- Name: Sales Closings
- Model: `account.sale.closing`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `company_id`, `cumulative_total`, `currency_id`, `date_closing_start`, `date_closing_stop`, `frequency`, `sequence_number`, `total_interval`
- XPath or positional patches: 0

## Actions

- `action_list_view_account_sale_closing`: `act_window` Sales Closings

## Menus

- `menu_account_closing_reporting`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/l10n_fr_pos_cert/Views]]

<!-- GENERATED:VIEWFILE -->
