<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/l10n_latam_document_type_view.xml

- Module: [[docs/Community Addons/l10n_ar/l10n_ar|l10n_ar]]
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
- Inherits: `l10n_latam_invoice_document.view_document_type_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `code`, `l10n_ar_letter`
- XPath or positional patches: 0

### `view_document_type_tree`
- Name: l10n_latam.document.type.list
- Model: `l10n_latam.document.type`
- Type: inferred from arch
- Inherits: `l10n_latam_invoice_document.view_document_type_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `doc_code_prefix`, `l10n_ar_letter`
- XPath or positional patches: 0

### `view_document_type_form`
- Name: l10n_latam.document.type.form
- Model: `l10n_latam.document.type`
- Type: inferred from arch
- Inherits: `l10n_latam_invoice_document.view_document_type_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `doc_code_prefix`, `l10n_ar_letter`, `purchase_aliquots`
- XPath or positional patches: 0

## Actions

- `action_document_type_argentina`: `act_window` Document Types

## Menus

- `menu_document_type_argentina`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ar/Views]]

<!-- GENERATED:VIEWFILE -->
