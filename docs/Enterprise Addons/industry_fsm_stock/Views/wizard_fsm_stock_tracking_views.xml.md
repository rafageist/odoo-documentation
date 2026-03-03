---
tags: [odoo, enterprise, generated, views]
---

# wizard/fsm_stock_tracking_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_stock/industry_fsm_stock|industry_fsm_stock]]
- Scope: Enterprise Addons
- Source file: `wizard/fsm_stock_tracking_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `fsm_stock_tracking_line_line_view_form`
- Name: fsm.stock.tracking.line.view.form
- Model: `fsm.stock.tracking.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `lot_id`, `product_id`, `quantity`, `sale_order_line_id`
- XPath or positional patches: 0

### `fsm_stock_tracking_line_view_form`
- Name: fsm.stock.tracking.view.form
- Model: `fsm.stock.tracking`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `company_id`, `is_same_warehouse`, `lot_id`, `product_id`, `quantity`, `sale_order_line_id`, `task_id`, `tracking`, `tracking_line_ids`, `tracking_validated_line_ids`, and 1 more
- Buttons: `generate_lot`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_stock/Views]]

