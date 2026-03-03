---
tags: [odoo, community, generated, views]
---

# views/stock_package_type_views.xml

- Module: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]
- Scope: Community Addons
- Source file: `views/stock_package_type_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_package_type_tree_delivery`
- Name: stock.package.type.list.delivery
- Model: `stock.package.type`
- Type: inferred from arch
- Inherits: `stock.stock_package_type_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `package_carrier_type`, `shipper_package_code`
- XPath or positional patches: 2

### `stock_package_type_form_delivery`
- Name: stock.package.type.form.delivery
- Model: `stock.package.type`
- Type: inferred from arch
- Inherits: `stock.stock_package_type_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `package_carrier_type`, `shipper_package_code`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/stock_delivery/Views]]

