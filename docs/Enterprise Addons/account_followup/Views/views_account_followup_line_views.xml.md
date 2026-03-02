<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_followup_line_views.xml

- Module: [[docs/Enterprise Addons/account_followup/account_followup|account_followup]]
- Scope: Enterprise Addons
- Source file: `views/account_followup_line_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_account_followup_line_filter`
- Name: account.followup.line.select
- Model: `account_followup.followup.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `company_id`
- XPath or positional patches: 0

### `view_account_followup_followup_line_form`
- Name: account_followup.followup.line.form
- Model: `account_followup.followup.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `activity_default_responsible_type`, `activity_note`, `activity_summary`, `activity_type_id`, `additional_follower_ids`, `auto_execute`, `create_activity`, `delay`, `join_invoices`, `mail_template_id`, and 4 more
- XPath or positional patches: 0

### `view_account_followup_followup_line_tree`
- Name: account_followup.followup.line.list
- Model: `account_followup.followup.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `activity_type_id`, `auto_execute`, `company_id`, `delay`, `name`, `send_email`, `send_sms`
- XPath or positional patches: 0

## Actions

- `action_account_followup_line_definition_form`: `act_window` Follow-up Levels

## Menus

- `account_followup_menu`: Follow-up Levels

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_followup/Views]]

<!-- GENERATED:VIEWFILE -->
