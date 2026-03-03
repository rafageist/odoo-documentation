---
tags: [odoo, enterprise, generated, views]
---

# views/studio_approval_views.xml

- Module: [[docs/Enterprise Addons/web_studio/web_studio|web_studio]]
- Scope: Enterprise Addons
- Source file: `views/studio_approval_views.xml`
- Views: 10
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `studio_approval_rule_delegate_approvers`
- Name: studio.approval.rule.delegate.form
- Model: `studio.approval.rule.delegate`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `approver_ids`, `date_to`, `users_to_notify`
- XPath or positional patches: 0

### `studio_approval_rule_search_view`
- Name: studio.approval.search
- Model: `studio.approval.rule`
- Type: inferred from arch
- Inherits: `studio_approval_rule_button_configuration_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

### `studio_approval_rule_button_configuration_search_view`
- Name: studio.approval.search
- Model: `studio.approval.rule`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `approval_group_id`, `approver_ids`, `name`
- XPath or positional patches: 0

### `studio_approval_rule_form_view`
- Name: studio.approval.form
- Model: `studio.approval.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `action_id`, `active`, `approval_group_id`, `approver_ids`, `domain`, `entries_count`, `exclusive_user`, `message`, `method`, `model_id`, and 3 more
- Buttons: `%(studio_approval_entry_action)d`, `open_delegate_action`
- XPath or positional patches: 0

### `studio_approval_rule_form_view_quick_create`
- Name: studio.approval.form.quick_create
- Model: `studio.approval.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `action_id`, `approval_group_id`, `approver_ids`, `exclusive_user`, `method`, `model_id`, `users_to_notify`
- XPath or positional patches: 0

### `studio_approval_rule_kanban_view`
- Name: studio.approval.kanban
- Model: `studio.approval.rule`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `approval_group_id`, `approver_ids`, `can_validate`, `exclusive_user`, `kanban_color`, `message`
- XPath or positional patches: 0

### `studio_approval_rule_tree_view`
- Name: studio.approval.list
- Model: `studio.approval.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `active`, `approval_group_id`, `approver_ids`, `message`, `model_id`, `name`
- XPath or positional patches: 0

### `studio_approval_entry_search_view`
- Name: studio.approval.entry.search
- Model: `studio.approval.entry`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `res_id`, `rule_id`, `user_id`
- XPath or positional patches: 0

### `studio_approval_entry_form_view`
- Name: studio.approval.entry.form
- Model: `studio.approval.entry`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `model`, `name`, `reference`, `res_id`, `rule_id`, `user_id`
- XPath or positional patches: 0

### `studio_approval_entry_tree_view`
- Name: studio.approval.entry.list
- Model: `studio.approval.entry`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `write_date`
- XPath or positional patches: 0

## Actions

- `studio_approval_rule_action`: `act_window` Studio Approval Rules
- `studio_approval_entry_action`: `act_window` Studio Approval Entries

## Menus

- `menu_studio_approval_rule`: Studio Approval Rules
- `menu_studio_approval_entry`: Studio Approval Entries

## Navigation

- **Parent:** [[docs/Enterprise Addons/web_studio/Views]]

