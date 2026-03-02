<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_return_type_views.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_return_type_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `account_return_type_search_view`
- Name: account.return.type.search.view
- Model: `account.return.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `category`, `country_id`, `deadline_periodicity`, `deadline_start_date`, `payment_partner_bank_id`, `payment_partner_id`, `report_id`
- XPath or positional patches: 0

### `account_return_type_list_view`
- Name: account.return.type.list.view
- Model: `account.return.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `category`, `country_id`, `deadline_periodicity`, `name`
- XPath or positional patches: 0

### `account_return_type_form_view`
- Name: account.return.type.form
- Model: `account.return.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `category`, `country_id`, `deadline_days_delay`, `deadline_periodicity`, `deadline_start_date`, `name`, `payment_partner_bank_id`, `payment_partner_id`, `report_id`, `states_workflow`
- XPath or positional patches: 0

## Actions

- `action_view_account_return_types`: `act_window` Return Types

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

<!-- GENERATED:VIEWFILE -->
