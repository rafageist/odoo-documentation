<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_return_check_views.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_return_check_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_return_check_search_view`
- Name: account.return.check.search
- Model: `account.return.check`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `cycle`, `name`, `result`, `return_id`, `template_id`, `type`
- XPath or positional patches: 0

### `account_return_check_kanban_view`
- Name: account.return.check.kanban
- Model: `account.return.check`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 13
- Sample fields: `action`, `approver_supervisor_ids`, `attachment_ids`, `cycle`, `message`, `name`, `records_count`, `records_name`, `result`, `return_id`, and 3 more
- Buttons: `action_unlink_attachments`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

<!-- GENERATED:VIEWFILE -->
