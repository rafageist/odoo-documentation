<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/account_invoice_extract/account_invoice_extract|account_invoice_extract]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_move_form_inherit_ocr`
- Name: invoice.move.form.inherit.ocr
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `extract_attachment_id`, `extract_can_show_banners`, `extract_can_show_send_button`, `extract_document_uuid`, `extract_error_message`, `extract_state`
- Buttons: `action_manual_send_for_digitization`, `action_reload_ai_data`
- XPath or positional patches: 4

## Actions

- `model_account_send_for_digitalization`: `server` Send Bills for digitization

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_invoice_extract/Views]]

<!-- GENERATED:VIEWFILE -->
