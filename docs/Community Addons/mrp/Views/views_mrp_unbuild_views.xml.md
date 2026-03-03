---
tags: [odoo, community, generated, views]
---

# views/mrp_unbuild_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/mrp_unbuild_views.xml`
- Views: 5
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `mrp_unbuild_tree_view`
- Name: mrp.unbuild.list
- Model: `mrp.unbuild`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `activity_exception_decoration`, `bom_id`, `company_id`, `location_id`, `lot_id`, `mo_id`, `name`, `product_id`, `product_qty`, `product_uom_id`, and 1 more
- XPath or positional patches: 0

### `mrp_unbuild_form_view_simplified`
- Name: mrp.unbuild.form.simplified
- Model: `mrp.unbuild`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `bom_id`, `company_id`, `has_tracking`, `location_dest_id`, `location_id`, `lot_id`, `mo_id`, `product_id`, `product_qty`, `product_uom_id`, and 1 more
- Buttons: `action_validate`
- XPath or positional patches: 0

### `mrp_unbuild_form_view`
- Name: mrp.unbuild.form
- Model: `mrp.unbuild`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `bom_id`, `company_id`, `has_tracking`, `location_dest_id`, `location_id`, `lot_id`, `mo_bom_id`, `mo_id`, `name`, `product_id`, and 3 more
- Buttons: `%(action_mrp_unbuild_moves)d`, `action_validate`
- XPath or positional patches: 0

### `mrp_unbuild_kanban_view`
- Name: mrp.unbuild.kanban
- Model: `mrp.unbuild`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `name`, `product_id`, `product_qty`, `product_uom_id`, `state`
- XPath or positional patches: 0

### `mrp_unbuild_search_view`
- Name: mrp.unbuild.search
- Model: `mrp.unbuild`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `mo_id`, `product_id`
- XPath or positional patches: 0

## Actions

- `mrp_unbuild`: `act_window` Unbuild Orders
- `action_mrp_unbuild_moves`: `act_window` Stock Moves

## Menus

- `menu_mrp_unbuild`: Unbuild Orders

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

