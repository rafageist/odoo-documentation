---
tags: [odoo, community, generated, views]
---

# views/stock_reference_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_reference_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `stock_reference_tree_view`
- Name: stock.reference.list
- Model: `stock.reference`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `stock_reference_form_view`
- Name: stock.reference.form
- Model: `stock.reference`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `name`, `picking_ids`
- XPath or positional patches: 0

### `stock_reference_search_view`
- Name: stock.reference.search
- Model: `stock.reference`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `action_stock_reference`: `act_window` References

## Menus

- `menu_stock_references`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

