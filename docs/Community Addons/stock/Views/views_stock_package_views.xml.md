<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_package_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_package_views.xml`
- Views: 6
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `stock_package_view_kanban`
- Name: stock.package.kanban
- Model: `stock.package`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `package_type_id`
- XPath or positional patches: 0

### `stock_package_view_add_list`
- Name: stock.package.add.package.list
- Model: `stock.package`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `content_description`, `display_name`, `location_id`, `package_type_id`
- Buttons: `action_add_to_picking`
- XPath or positional patches: 0

### `stock_package_view_list_editable`
- Name: stock.package.list.editable
- Model: `stock.package`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `json_popover`, `location_dest_id`, `name`, `package_dest_id`, `package_type_id`, `parent_package_id`
- Buttons: `action_put_in_pack`, `action_remove_package`
- XPath or positional patches: 0

### `stock_package_view_list`
- Name: stock.package.list
- Model: `stock.package`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `location_id`, `name`, `package_type_id`, `parent_package_id`
- XPath or positional patches: 0

### `stock_package_view_form`
- Name: stock.package.form
- Model: `stock.package`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `company_id`, `contained_quant_ids`, `location_id`, `lot_id`, `name`, `owner_id`, `pack_date`, `package_id`, `package_type_id`, `parent_package_id`, and 3 more
- Buttons: `action_view_picking`, `unpack`
- XPath or positional patches: 0

### `stock_package_view_search`
- Name: stock.package.search
- Model: `stock.package`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `location_id`, `name`, `package_type_id`
- XPath or positional patches: 0

## Actions

- `action_package_view`: `act_window` Packages

## Menus

- `menu_package`: Packages

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
