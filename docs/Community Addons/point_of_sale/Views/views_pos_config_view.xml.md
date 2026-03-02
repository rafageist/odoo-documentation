<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/pos_config_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_config_view.xml`
- Views: 3
- Actions: 2
- Menus: 4
- Rules: 0

## View records

### `view_pos_config_search`
- Name: pos.config.search.view
- Model: `pos.config`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `picking_type_id`
- XPath or positional patches: 0

### `view_pos_config_tree`
- Name: pos.config.list.view
- Model: `pos.config`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `currency_id`, `last_session_closing_cash`, `last_session_closing_date`, `name`
- XPath or positional patches: 0

### `pos_config_view_form`
- Name: pos.config.form.view
- Model: `pos.config`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `active`, `company_has_template`, `epson_printer_ip`, `has_active_session`, `iface_cashdrawer`, `iface_electronic_scale`, `iface_print_via_proxy`, `iface_scan_via_proxy`, `is_posbox`, `module_pos_hr`, and 4 more
- Buttons: `open_ui`
- XPath or positional patches: 0

## Actions

- `action_pos_config_tree`: `act_window` Point of Sale List
- `action_pos_config_kanban`: `act_window` Point of Sale

## Menus

- `menu_point_of_sale_list`: Point of Sales
- `menu_pos_dashboard`: Dashboard
- `pos_menu_products_attribute_action`: unnamed
- `menu_products_pos_category`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

<!-- GENERATED:VIEWFILE -->
