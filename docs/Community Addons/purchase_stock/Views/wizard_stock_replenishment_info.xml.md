---
tags: [odoo, community, generated, views]
---

# wizard/stock_replenishment_info.xml

- Module: [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
- Scope: Community Addons
- Source file: `wizard/stock_replenishment_info.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_replenishment_info_stock_purchase_inherit`
- Name: stock.replenishment.information.purchase.stock.inherit
- Model: `stock.replenishment.info`
- Type: inferred from arch
- Inherits: `stock.view_stock_replenishment_info`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `supplierinfo_id`, `supplierinfo_ids`
- XPath or positional patches: 1

### `product_supplierinfo_replenishment_tree_view`
- Name: product.supplierinfo.replenishment.list.view
- Model: `product.supplierinfo`
- Type: inferred from arch
- Inherits: `product.product_supplierinfo_tree_view`
- Root tag: `field`
- Field references: 7
- Sample fields: `company_id`, `delay`, `last_purchase_date`, `min_qty`, `product_uom_id`, `sequence`, `show_set_supplier_button`
- Buttons: `action_set_supplier`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/purchase_stock/Views]]

