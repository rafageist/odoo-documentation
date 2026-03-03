---
tags: [odoo, enterprise, generated, views]
---

# views/pos_order_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi_pos/l10n_mx_edi_pos|l10n_mx_edi_pos]]
- Scope: Enterprise Addons
- Source file: `views/pos_order_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `pos_order_tree_inherit_l10n_mx_edi`
- Name: pos.order.list.inherit.l10n_mx_edi
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `l10n_mx_edi_cfdi_sat_state`, `l10n_mx_edi_cfdi_state`, `l10n_mx_edi_cfdi_uuid`, `state`
- XPath or positional patches: 0

### `pos_order_form_inherit_l10n_mx_edi`
- Name: pos.order.form
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `xpath`
- Field references: 19
- Sample fields: `attachment_id`, `attachment_origin`, `attachment_uuid`, `cancel_button_needed`, `cancellation_reason`, `datetime`, `l10n_mx_edi_cfdi_sat_state`, `l10n_mx_edi_cfdi_state`, `l10n_mx_edi_cfdi_to_public`, `l10n_mx_edi_cfdi_uuid`, and 9 more
- Buttons: `action_cancel`, `action_download_file`, `action_retry`, `action_show_document`, `l10n_mx_edi_cfdi_try_sat`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi_pos/Views]]

