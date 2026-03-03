---
tags: [odoo, community, generated, views]
---

# wizard/product_replenish_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `wizard/product_replenish_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_product_replenish`
- Name: Replenish
- Model: `product.replenish`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `allowed_route_ids`, `company_id`, `date_planned`, `forecast_uom_id`, `forecasted_quantity`, `product_has_variants`, `product_id`, `product_tmpl_id`, `product_uom_id`, `quantity`, and 2 more
- Buttons: `launch_replenishment`
- XPath or positional patches: 0

## Actions

- `action_product_replenish`: `act_window` Low on stock? Let's replenish.

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

