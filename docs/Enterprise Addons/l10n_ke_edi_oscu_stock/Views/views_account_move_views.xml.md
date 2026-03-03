---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `invoice_form_inherit_l10n_ke_oscu_stock`
- Name: invoice.form.inherit.l10n.ke.edi.oscu.stock
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `l10n_ke_oscu_attachment_file`, `l10n_ke_oscu_invoice_number`, `l10n_ke_oscu_show_create_purchase_order_button`, `l10n_ke_oscu_show_create_sale_order_button`, `purchase_line_id`
- Buttons: `action_l10n_ke_create_purchase_order`, `action_l10n_ke_create_sale_order`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/Views]]

