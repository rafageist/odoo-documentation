<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/l10n_latam_document_type_view.xml

- Module: [[docs/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]]
- Scope: Community Addons
- Source file: `views/l10n_latam_document_type_view.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_document_type_filter`
- Name: l10n_latam.document.type.filter
- Model: `l10n_latam.document.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `code`, `country_id`, `internal_type`, `name`
- XPath or positional patches: 0

### `view_document_type_tree`
- Name: l10n_latam.document.type.list
- Model: `l10n_latam.document.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `active`, `code`, `country_id`, `doc_code_prefix`, `internal_type`, `name`, `report_name`
- XPath or positional patches: 0

### `view_document_type_form`
- Name: l10n_latam.document.type.form
- Model: `l10n_latam.document.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `code`, `country_id`, `doc_code_prefix`, `internal_type`, `name`, `report_name`
- XPath or positional patches: 0

## Actions

- `action_document_type`: `act_window` Document Types

## Menus

- `menu_document_type`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/l10n_latam_invoice_document/Views]]

<!-- GENERATED:VIEWFILE -->
