---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu/l10n_ke_edi_oscu|l10n_ke_edi_oscu]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `invoice_form_inherit_l10n_ke_oscu`
- Name: invoice.form.inherit.l10n.ke.oscu
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `l10n_ke_oscu_datetime`, `l10n_ke_oscu_internal_data`, `l10n_ke_oscu_invoice_number`, `l10n_ke_oscu_receipt_number`, `l10n_ke_oscu_signature`, `l10n_ke_payment_method_id`, `l10n_ke_reason_code_id`, `l10n_ke_validation_message`, `reversed_entry_id`
- Buttons: `action_l10n_ke_oscu_confirm_vendor_bill`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu/Views]]

