---
tags: [odoo, enterprise, generated, views]
---

# views/pos_order.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_pos/l10n_ke_edi_oscu_pos|l10n_ke_edi_oscu_pos]]
- Scope: Enterprise Addons
- Source file: `views/pos_order.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_pos_order_filter`
- Name: pos.order.list.select
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_pos_order_tree`
- Name: pos.order.list
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ke_order_send_status`
- XPath or positional patches: 2

### `view_pos_pos_form`
- Name: pos.order
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `l10n_ke_order_send_status`, `l10n_ke_oscu_confirmation_datetime`, `l10n_ke_oscu_datetime`, `l10n_ke_oscu_internal_data`, `l10n_ke_oscu_order_number`, `l10n_ke_oscu_receipt_number`, `l10n_ke_oscu_signature`
- Buttons: `action_post_order`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_pos/Views]]

