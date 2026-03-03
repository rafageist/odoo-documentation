---
tags: [odoo, community, generated, views]
---

# views/myinvois_document_views.xml

- Module: [[docs/Community Addons/l10n_my_edi/l10n_my_edi|l10n_my_edi]]
- Scope: Community Addons
- Source file: `views/myinvois_document_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `myinvois_document_list_view`
- Name: myinvois.document.list.view
- Model: `myinvois.document`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `display_name`, `myinvois_issuance_date`, `myinvois_state`
- Buttons: `action_submit_to_myinvois`, `action_update_submission_status`
- XPath or positional patches: 0

### `myinvois_document_form_view`
- Name: myinvois.document.form.view
- Model: `myinvois.document`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `display_name`, `myinvois_custom_form_reference`, `myinvois_exemption_reason`, `myinvois_external_uuid`, `myinvois_issuance_date`, `myinvois_state`, `myinvois_submission_uid`, `myinvois_validation_time`
- Buttons: `action_cancel_submission`, `action_submit_to_myinvois`, `action_update_submission_status`
- XPath or positional patches: 0

## Actions

- `action_generate_myinvois_document_file`: `server` Generate Document File

## Navigation

- **Parent:** [[docs/Community Addons/l10n_my_edi/Views]]

