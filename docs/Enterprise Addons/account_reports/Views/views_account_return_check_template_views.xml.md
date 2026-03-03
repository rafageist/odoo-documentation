---
tags: [odoo, enterprise, generated, views]
---

# views/account_return_check_template_views.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_return_check_template_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `account_return_check_template_search_view`
- Name: account.return.check.template.search
- Model: `account.return.check.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `cycle`, `name`, `return_type`
- XPath or positional patches: 0

### `account_return_check_template_form_view`
- Name: account.return.check.template.form
- Model: `account.return.check.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `action_id`, `activity_type`, `cycle`, `description`, `domain`, `model`, `name`, `return_type`, `type`
- XPath or positional patches: 0

### `account_return_check_template_list_view`
- Name: account.return.check.template.list
- Model: `account.return.check.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `cycle`, `name`, `return_type`, `type`
- XPath or positional patches: 0

## Actions

- `action_view_account_return_check_templates`: `act_window` Check Templates

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

