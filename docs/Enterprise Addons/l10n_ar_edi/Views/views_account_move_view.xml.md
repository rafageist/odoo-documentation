<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Enterprise Addons/l10n_ar_edi/l10n_ar_edi|l10n_ar_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_move_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_form_ar`
- Name: account.move.form.2
- Model: `account.move`
- Type: inferred from arch
- Inherits: `l10n_ar.view_move_form`
- Root tag: `group`
- Field references: 3
- Sample fields: `l10n_ar_afip_fce_is_cancellation`, `l10n_ar_fce_transmission_type`, `l10n_latam_document_type_id_code`
- XPath or positional patches: 1

### `view_move_form`
- Name: account.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `l10n_latam_invoice_document.view_move_form`
- Root tag: `form`
- Field references: 14
- Sample fields: `l10n_ar_afip_auth_code`, `l10n_ar_afip_auth_code_due`, `l10n_ar_afip_auth_mode`, `l10n_ar_afip_result`, `l10n_ar_afip_verification_result`, `l10n_ar_afip_verification_type`, `l10n_ar_afip_ws`, `l10n_ar_afip_xml_request`, `l10n_ar_afip_xml_response`, `l10n_ar_currency_code`, and 4 more
- Buttons: `l10n_ar_verify_on_afip`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ar_edi/Views]]

<!-- GENERATED:VIEWFILE -->
