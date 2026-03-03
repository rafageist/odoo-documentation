---
tags: [odoo, enterprise, generated, views]
---

# views/approval_category_views.xml

- Module: [[docs/Enterprise Addons/approvals/approvals|approvals]]
- Scope: Enterprise Addons
- Source file: `views/approval_category_views.xml`
- Views: 4
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `approval_category_view_kanban`
- Name: approval.category.views.kanban
- Model: `approval.category`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `active`, `description`, `image`, `name`, `request_to_validate_count`
- Buttons: `%(approvals.approval_request_action_to_review_category)d`, `create_request`
- XPath or positional patches: 0

### `approval_category_view_form`
- Name: approval.category.view.form
- Model: `approval.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 24
- Sample fields: `active`, `approval_minimum`, `approval_type`, `approver_ids`, `approver_sequence`, `automated_sequence`, `company_id`, `description`, `has_amount`, `has_date`, and 14 more
- XPath or positional patches: 0

### `approval_category_view_search`
- Name: approval.category.search
- Model: `approval.category`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `approval_category_view_tree`
- Name: approval.category.view.list
- Model: `approval.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `action_open_approval_category`: `server` Open Approval Category
- `approval_request_action_to_review_category`: `act_window` Approvals to review
- `approval_category_action`: `act_window` Approval Categories
- `approval_category_action_new_request`: `act_window` Dashboard

## Navigation

- **Parent:** [[docs/Enterprise Addons/approvals/Views]]

