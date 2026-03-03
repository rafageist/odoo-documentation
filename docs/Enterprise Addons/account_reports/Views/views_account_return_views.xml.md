---
tags: [odoo, enterprise, generated, views]
---

# views/account_return_views.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_return_views.xml`
- Views: 3
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `account_return_search_view`
- Name: account.return
- Model: `account.return`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `date_deadline`, `date_from`, `date_submission`, `date_to`, `name`, `state`, `type_id`
- XPath or positional patches: 0

### `account_return_calendar_view`
- Name: account.return.calendar
- Model: `account.return`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 2
- Sample fields: `name`, `type_id`
- XPath or positional patches: 0

### `account_return_kanban_view`
- Name: account.return.kanban
- Model: `account.return`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 27
- Sample fields: `active`, `activity_ids`, `amount_to_pay_currency_id`, `check_ids`, `company_ids`, `date_deadline`, `date_submission`, `days_to_deadline`, `has_move_entries`, `is_completed`, and 17 more
- Buttons: `action_open_attachments`, `action_open_report`, `action_pay`, `action_submit`, `action_validate`
- XPath or positional patches: 0

## Actions

- `action_create_account_return`: `act_window` Generate Return
- `action_view_account_return`: `act_window` Tax Return
- `action_server_open_view_account_return`: `server` Open Tax Return

## Menus

- `menu_action_account_return`: Tax Returns

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

