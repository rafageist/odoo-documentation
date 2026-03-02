<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_move_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `invoice_status_form_cl`
- Name: account.move.invoice.status.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `l10n_latam_invoice_document.view_move_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `l10n_cl_dte_acceptation_status`, `l10n_cl_dte_status`
- Buttons: `l10n_cl_reprocess_acknowledge`, `l10n_cl_send_dte_to_sii`, `l10n_cl_verify_claim_status`, `l10n_cl_verify_dte_status`
- XPath or positional patches: 1

### `view_invoice_form`
- Name: account.move.edi.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `date`, `l10n_cl_dte_acceptation_status`, `l10n_cl_dte_partner_status`, `l10n_cl_dte_status`, `l10n_cl_reference_doc_internal_type`, `l10n_cl_reference_doc_type_id`, `l10n_cl_reference_ids`, `l10n_cl_sii_send_ident`, `origin_doc_number`, `reason`, and 1 more
- Buttons: `l10n_cl_accept_document`, `l10n_cl_claim_document`, `l10n_cl_receipt_service_or_merchandise`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_cl_edi/Views]]

<!-- GENERATED:VIEWFILE -->
