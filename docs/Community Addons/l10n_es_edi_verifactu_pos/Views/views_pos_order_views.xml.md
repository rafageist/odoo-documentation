<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/pos_order_views.xml

- Module: [[docs/Community Addons/l10n_es_edi_verifactu_pos/l10n_es_edi_verifactu_pos|l10n_es_edi_verifactu_pos]]
- Scope: Community Addons
- Source file: `views/pos_order_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_pos_order_form_inherit_l10n_es_pos_verifactu`
- Name: pos.order.form.inherit.l10n_es_edi_verifactu_pos
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `create_date`, `document_type`, `id`, `l10n_es_edi_verifactu_document_ids`, `l10n_es_edi_verifactu_refund_reason`, `l10n_es_edi_verifactu_state`, `l10n_es_edi_verifactu_warning`, `state`
- Buttons: `l10n_es_edi_verifactu_button_send`
- XPath or positional patches: 3

### `view_pos_order_tree`
- Name: pos.order.tree
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_es_edi_verifactu_state`, `state`
- XPath or positional patches: 0

### `view_pos_order_filter`
- Name: pos.order.list.select
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_es_edi_verifactu_pos/Views]]

<!-- GENERATED:VIEWFILE -->
