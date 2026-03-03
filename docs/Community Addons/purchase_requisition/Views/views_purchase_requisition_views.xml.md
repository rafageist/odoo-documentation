---
tags: [odoo, community, generated, views]
---

# views/purchase_requisition_views.xml

- Module: [[docs/Community Addons/purchase_requisition/purchase_requisition|purchase_requisition]]
- Scope: Community Addons
- Source file: `views/purchase_requisition_views.xml`
- Views: 4
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `view_purchase_requisition_filter`
- Name: purchase.requisition.list.select
- Model: `purchase.requisition`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `product_id`, `user_id`, `vendor_id`
- XPath or positional patches: 0

### `view_purchase_requisition_kanban`
- Name: purchase.requisition.kanban
- Model: `purchase.requisition`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `name`, `requisition_type`, `state`, `user_id`, `vendor_id`
- XPath or positional patches: 0

### `view_purchase_requisition_tree`
- Name: purchase.requisition.list
- Model: `purchase.requisition`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `activity_exception_decoration`, `company_id`, `date_end`, `date_start`, `message_needaction`, `name`, `reference`, `requisition_type`, `state`, `user_id`, and 1 more
- XPath or positional patches: 0

### `view_purchase_requisition_form`
- Name: purchase.requisition.form
- Model: `purchase.requisition`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `active`, `analytic_distribution`, `company_id`, `currency_id`, `date_end`, `date_start`, `description`, `line_ids`, `name`, `order_count`, and 11 more
- Buttons: `%(action_purchase_requisition_list)d`, `%(action_purchase_requisition_to_so)d`, `action_cancel`, `action_confirm`, `action_done`, `action_draft`
- XPath or positional patches: 0

## Actions

- `action_purchase_requisition`: `act_window` Purchase Agreements
- `action_purchase_requisition_list`: `act_window` Request for Quotations
- `action_purchase_requisition_to_so`: `act_window` Request for Quotation

## Menus

- `menu_purchase_requisition_pro_mgt`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/purchase_requisition/Views]]

