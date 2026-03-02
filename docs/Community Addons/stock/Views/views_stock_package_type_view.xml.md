<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_package_type_view.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_package_type_view.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `stock_package_type_tree`
- Name: stock.package.type.list
- Model: `stock.package.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `barcode`, `has_quants`, `height`, `max_weight`, `name`, `packaging_length`, `sequence`, `width`
- XPath or positional patches: 0

### `stock_package_type_form`
- Name: stock.package.type.form
- Model: `stock.package.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `barcode`, `base_weight`, `company_id`, `height`, `length_uom_name`, `max_weight`, `name`, `packaging_length`, `quantity`, `route_ids`, and 6 more
- XPath or positional patches: 0

## Actions

- `action_package_type_view`: `act_window` Package Types

## Menus

- `menu_packaging_types`: Package Types
- `menu_delivery`: Delivery

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
