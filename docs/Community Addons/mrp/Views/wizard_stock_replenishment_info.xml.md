<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/stock_replenishment_info.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `wizard/stock_replenishment_info.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_replenishment_info_stock_mrp_inherit`
- Name: stock.replenishment.information.mrp.stock.inherit
- Model: `stock.replenishment.info`
- Type: inferred from arch
- Inherits: `stock.view_stock_replenishment_info`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `bom_id`, `bom_ids`
- XPath or positional patches: 1

### `mrp_bom_replenishment_tree_view`
- Name: mrp.bom.replenishment.list.view
- Model: `mrp.bom`
- Type: inferred from arch
- Inherits: `mrp.mrp_bom_tree_view`
- Root tag: `field`
- Field references: 3
- Sample fields: `company_id`, `product_uom_id`, `show_set_bom_button`
- Buttons: `action_set_bom_on_orderpoint`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

<!-- GENERATED:VIEWFILE -->
