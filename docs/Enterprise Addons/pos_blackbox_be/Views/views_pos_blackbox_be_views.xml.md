---
tags: [odoo, enterprise, generated, views]
---

# views/pos_blackbox_be_views.xml

- Module: [[docs/Enterprise Addons/pos_blackbox_be/pos_blackbox_be|pos_blackbox_be]]
- Scope: Enterprise Addons
- Source file: `views/pos_blackbox_be_views.xml`
- Views: 7
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_pos_order_filter_registered_transactions`
- Name: pos.order.list.select
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_filter`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 1

### `pos_config_view_form_inherit_pos_blackbox_be`
- Name: pos.config.form.inherit.blackbox.be
- Model: `pos.config`
- Type: inferred from arch
- Inherits: `pos_iot.pos_iot_config_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `iface_fiscal_data_module`
- XPath or positional patches: 2

### `view_pos_config_kanban`
- Name: pos.config.kanban.view.inherit.pos_blackbox_be
- Model: `pos.config`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_config_kanban`
- Root tag: `field`
- Field references: 3
- Sample fields: `certified_blackbox_identifier`, `name`, `pos_version`
- XPath or positional patches: 0

### `view_pos_blackbox_be_log_tree`
- Name: Log book
- Model: `pos_blackbox_be.log`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `action`, `date`, `description`, `model_name`, `record_name`, `user`
- XPath or positional patches: 0

### `view_pos_order_tree`
- Name: pos.order.list.view.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_pos_order_kanban`
- Name: pos.order.kanban.view.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_pos_pos_form`
- Name: pos.order.form.view.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `action_log_book_form`: `act_window` Log book

## Menus

- `menu_log_book`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_blackbox_be/Views]]

