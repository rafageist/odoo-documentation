---
tags: [odoo, enterprise, generated, views]
---

# wizard/documents_request_wizard_views.xml

- Module: [[docs/Enterprise Addons/documents/documents|documents]]
- Scope: Enterprise Addons
- Source file: `wizard/documents_request_wizard_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `documents_request_form_view`
- Name: Request File
- Model: `documents.request_wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `activity_date_deadline_range`, `activity_date_deadline_range_type`, `activity_note`, `activity_type_id`, `folder_id`, `name`, `partner_id`, `requestee_id`, `res_id`, `res_model`, and 1 more
- Buttons: `request_document`
- XPath or positional patches: 0

## Actions

- `action_request_form`: `act_window` Request a file

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents/Views]]

