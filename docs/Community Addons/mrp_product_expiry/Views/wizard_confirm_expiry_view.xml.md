---
tags: [odoo, community, generated, views]
---

# wizard/confirm_expiry_view.xml

- Module: [[docs/Community Addons/mrp_product_expiry/mrp_product_expiry|mrp_product_expiry]]
- Scope: Community Addons
- Source file: `wizard/confirm_expiry_view.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `confirm_expiry_view_mrp_inherit`
- Name: Confirm
- Model: `expiry.picking.confirmation`
- Type: inferred from arch
- Inherits: `product_expiry.confirm_expiry_view`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `picking_ids`, `production_ids`, `workorder_id`
- Buttons: `confirm_produce`, `confirm_workorder`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Community Addons/mrp_product_expiry/Views]]

