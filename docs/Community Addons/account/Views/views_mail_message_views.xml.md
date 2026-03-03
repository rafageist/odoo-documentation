<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_message_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/mail_message_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_message_tree_audit_log_search`
- Name: mail.message.search
- Model: `mail.message`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `account_audit_log_account_id`, `account_audit_log_company_id`, `account_audit_log_move_id`, `account_audit_log_partner_id`, `account_audit_log_tax_id`, `author_id`, `date`, `tracking_value_ids`
- XPath or positional patches: 0

### `view_message_tree_audit_log`
- Name: mail.message.list.inherit.audit.log
- Model: `mail.message`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `account_audit_log_preview`, `author_id`, `date`, `res_id`
- XPath or positional patches: 0

## Actions

- `action_account_audit_trail_report`: `act_window` Audit Trail

## Menus

- `account_audit_trail_menu`: Audit Trail

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
