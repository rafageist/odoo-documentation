<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/pos_order_view.xml

- Module: [[docs/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/pos_order_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_pos_order_tree`
- Name: pos.order.list
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `avg_preparation_time`, `avg_service_time`
- XPath or positional patches: 1

### `view_pos_pos_form`
- Name: pos.order.form.view.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `preparation_time`, `service_time`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
