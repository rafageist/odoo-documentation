<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# sale.pdf.form.field

- Module: [[docs/Community Addons/sale_pdf_quote_builder/sale_pdf_quote_builder|sale_pdf_quote_builder]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/sale_pdf_form_field.py`
- Python classes: `SalePdfFormField`
- Description: Form fields of inside quotation documents.

## Field footprint

- Detected fields: 5
- Field types: `Char` x 2, `Many2many` x 2, `Selection` x 1
- Relation fields: 2

## Sample fields

- `document_type`: `Selection`
- `name`: `Char`
- `path`: `Char`
- `product_document_ids`: `Many2many` (comodel `product.document`)
- `quotation_document_ids`: `Many2many` (comodel `quotation.document`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title sale.pdf.form.field - Direct Relations
class "sale.pdf.form.field" as sale_pdf_form_field
class "product.document" as product_document
class "quotation.document" as quotation_document
sale_pdf_form_field .. product_document : product_document_ids
sale_pdf_form_field .. quotation_document : quotation_document_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/sale_pdf_quote_builder/Models]]

<!-- GENERATED:MODEL -->
