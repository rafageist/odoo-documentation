<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/approval_request_views.xml

- Module: [[docs/Enterprise Addons/approvals/approvals|approvals]]
- Scope: Enterprise Addons
- Source file: `views/approval_request_views.xml`
- Views: 4
- Actions: 4
- Menus: 12
- Rules: 0

## View records

### `approval_request_view_kanban`
- Name: approval.request.view.kanban
- Model: `approval.request`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `activity_ids`, `category_image`, `date_end`, `date_start`, `name`, `request_owner_id`, `request_status`, `user_status`
- Buttons: `action_approve`, `action_refuse`
- XPath or positional patches: 0

### `approval_request_view_form`
- Name: approval.request.view.form
- Model: `approval.request`
- Type: inferred from arch
- Root tag: `form`
- Field references: 44
- Sample fields: `active`, `amount`, `approval_minimum`, `approval_properties`, `approval_type`, `approver_ids`, `attachment_number`, `automated_sequence`, `can_edit`, `can_edit_user_id`, and 34 more
- Buttons: `%(action_report_approval_request)d`, `action_approve`, `action_cancel`, `action_confirm`, `action_draft`, `action_get_attachment_view`, `action_refuse`, `action_withdraw`
- XPath or positional patches: 0

### `approval_search_view_search`
- Name: approval.request.search
- Model: `approval.request`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `approval_request_view_tree`
- Name: approval.request.view.list
- Model: `approval.request`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `activity_ids`, `approval_properties`, `category_id`, `company_id`, `date_confirmed`, `date_end`, `date_start`, `location`, `name`, `request_owner_id`, and 2 more
- XPath or positional patches: 0

## Actions

- `model_approval_request_approve_admin`: `server` Force Approval
- `approval_request_action_all`: `act_window` All Approvals
- `approval_request_action_to_review`: `act_window` Approvals to Review
- `approval_request_action`: `act_window` My Requests

## Menus

- `approvals_menu_product_variant`: Product Variants
- `approvals_menu_product_template`: Products
- `approvals_menu_product`: Products
- `approvals_category_menu_config`: Approval Categories
- `approvals_menu_config`: Configuration
- `approvals_approval_menu_all`: All Approvals
- `approvals_approval_menu_to_review`: Approvals to Review
- `approvals_menu_manager`: Manager
- `approvals_request_menu_my`: My Requests
- `approvals_approval_menu`: My Approvals
- `approvals_category_menu_new`: Dashboard
- `approvals_menu_root`: Approvals

## Navigation

- **Parent:** [[docs/Enterprise Addons/approvals/Views]]

<!-- GENERATED:VIEWFILE -->
