<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/quotation_document_views.xml

- Module: [[docs/Community Addons/sale_pdf_quote_builder/sale_pdf_quote_builder|sale_pdf_quote_builder]]
- Scope: Community Addons
- Source file: `views/quotation_document_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `quotation_document_search_view`
- Name: quotation.document.search
- Model: `quotation.document`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `quotation_document_list`
- Name: quotation.document.list
- Model: `quotation.document`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `add_by_default`, `company_id`, `document_type`, `name`, `quotation_template_ids`, `sequence`
- XPath or positional patches: 0

### `quotation_document_kanban`
- Name: quotation.document.kanban
- Model: `quotation.document`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `active`, `document_type`, `ir_attachment_id`, `mimetype`, `name`, `quotation_template_ids`, `sequence`
- XPath or positional patches: 0

### `quotation_document_form`
- Name: quotation.document.form
- Model: `quotation.document`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `add_by_default`, `company_id`, `create_date`, `create_uid`, `datas`, `document_type`, `form_field_ids`, `name`, `quotation_template_ids`
- Buttons: `action_open_pdf_form_fields`
- XPath or positional patches: 0

## Actions

- `quotation_document_action`: `act_window` Headers/Footers

## Navigation

- **Parent:** [[docs/Community Addons/sale_pdf_quote_builder/Views]]

<!-- GENERATED:VIEWFILE -->
