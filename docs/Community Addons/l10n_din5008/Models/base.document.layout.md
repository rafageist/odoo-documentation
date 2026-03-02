<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# base.document.layout

- Module: [[docs/Community Addons/l10n_din5008/l10n_din5008|l10n_din5008]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/base_document_layout.py`
- Python classes: `BaseDocumentLayout`

## Field footprint

- Detected fields: 12
- Field types: `Char` x 5, `Date` x 3, `Html` x 2, `Many2one` x 1, `One2many` x 1
- Relation fields: 2

## Sample fields

- `account_fiscal_country_id`: `Many2one` (related `company_id.account_fiscal_country_id`)
- `bank_ids`: `One2many` (related `company_id.partner_id.bank_ids`)
- `city`: `Char` (related `company_id.city`)
- `company_details`: `Html`
- `company_registry`: `Char` (related `company_id.company_registry`)
- `l10n_din5008_delivery_date`: `Date` (store `False`)
- `l10n_din5008_due_date`: `Date` (store `False`)
- `l10n_din5008_invoice_date`: `Date` (store `False`)
- `report_footer`: `Html`
- `street`: `Char` (related `company_id.street`)
- `street2`: `Char` (related `company_id.street2`)
- `zip`: `Char` (related `company_id.zip`)

## Method hints

- Detected methods: 2
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
title base.document.layout - Direct Relations
class "base.document.layout" as base_document_layout
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_din5008/Models]]

<!-- GENERATED:MODEL -->
