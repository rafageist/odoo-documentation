---
tags: [odoo, enterprise, generated, views]
---

# wizard/l10n_mx_edi_global_invoice_create.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi_pos/l10n_mx_edi_pos|l10n_mx_edi_pos]]
- Scope: Enterprise Addons
- Source file: `wizard/l10n_mx_edi_global_invoice_create.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_mx_edi_global_invoice_create_form_inherit_l10n_mx_edi_pos`
- Name: l10n_mx_edi.global_invoice.create.form.inherit.l10n_mx_edi_pos
- Model: `l10n_mx_edi.global_invoice.create`
- Type: inferred from arch
- Inherits: `l10n_mx_edi.l10n_mx_edi_global_invoice_create_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `move_ids`, `pos_order_ids`
- XPath or positional patches: 0

## Actions

- `action_account_move_create_global_invoice`: `server` Create Global Invoice

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi_pos/Views]]

