<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Community Addons/l10n_eg_edi_eta/l10n_eg_edi_eta|l10n_eg_edi_eta]]
- Scope: Community Addons
- Source file: `views/account_move_view.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_move_form_inherit`
- Name: view_move_form_inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `l10n_eg_eta_json_doc_file`, `l10n_eg_is_signed`, `l10n_eg_submission_number`, `l10n_eg_uuid`
- Buttons: `action_get_eta_invoice_pdf`, `action_post_sign_invoices`
- XPath or positional patches: 2

## Actions

- `action_sign_invoices`: `server` Sign invoices

## Navigation

- **Parent:** [[docs/Community Addons/l10n_eg_edi_eta/Views]]

<!-- GENERATED:VIEWFILE -->
