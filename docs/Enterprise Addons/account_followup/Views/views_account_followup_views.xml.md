---
tags: [odoo, enterprise, generated, views]
---

# views/account_followup_views.xml

- Module: [[docs/Enterprise Addons/account_followup/account_followup|account_followup]]
- Scope: Enterprise Addons
- Source file: `views/account_followup_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `customer_statements_search_view`
- Name: customer.statements.search
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `customer_statements_tree_view`
- Name: customer.statements.list
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_tree`
- Root tag: `list`
- Field references: 7
- Sample fields: `followup_line_id`, `followup_next_action_date`, `followup_reminder_type`, `followup_responsible_id`, `followup_status`, `total_due`, `total_overdue`
- XPath or positional patches: 1

## Actions

- `action_account_reports_customer_statements_do_followup`: `server` Process Follow-ups

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_followup/Views]]

