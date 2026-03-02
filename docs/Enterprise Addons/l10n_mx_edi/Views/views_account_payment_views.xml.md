<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_payment_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_payment_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_payment_tree_inherit_l10n_mx_edi`
- Name: account.payment.list.inherit.l10n_mx_edi
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `l10n_mx_edi_cfdi_sat_state`, `l10n_mx_edi_cfdi_state`, `l10n_mx_edi_cfdi_uuid`, `state`
- XPath or positional patches: 0

### `account_payment_form_inherit_l10n_mx_edi`
- Name: account.payment.form.inherit.l10n_mx_edi
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_form`
- Root tag: `xpath`
- Field references: 17
- Sample fields: `attachment_id`, `cancel_button_needed`, `cancellation_reason`, `datetime`, `l10n_mx_edi_cfdi_cancel_id`, `l10n_mx_edi_cfdi_origin`, `l10n_mx_edi_cfdi_sat_state`, `l10n_mx_edi_cfdi_state`, `l10n_mx_edi_cfdi_uuid`, `l10n_mx_edi_force_pue_payment_needed`, and 7 more
- Buttons: `action_cancel`, `action_download_file`, `action_download_payment_receipt`, `action_force_payment_cfdi`, `action_retry`, `l10n_mx_edi_cfdi_payment_force_try_send`, `l10n_mx_edi_cfdi_try_sat`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi/Views]]

<!-- GENERATED:VIEWFILE -->
