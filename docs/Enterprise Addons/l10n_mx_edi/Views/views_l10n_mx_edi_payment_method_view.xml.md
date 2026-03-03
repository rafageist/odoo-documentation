---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_mx_edi_payment_method_view.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]]
- Scope: Enterprise Addons
- Source file: `views/l10n_mx_edi_payment_method_view.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_l10n_mx_payment_method_tree`
- Name: view.l10n_mx.payment.method.list
- Model: `l10n_mx_edi.payment.method`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `code`, `name`
- XPath or positional patches: 0

### `view_l10n_mx_payment_method_form`
- Name: view.l10n_mx.payment.method.form
- Model: `l10n_mx_edi.payment.method`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `active`, `code`, `name`
- XPath or positional patches: 0

## Actions

- `action_l10n_mx_payment_method`: `act_window` Payment Way

## Menus

- `cfd_22_metodos_pago`: Payment Way Codes (MX)

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi/Views]]

