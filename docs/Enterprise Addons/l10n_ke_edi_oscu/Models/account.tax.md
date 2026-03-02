<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.tax

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu/l10n_ke_edi_oscu|l10n_ke_edi_oscu]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_tax.py`
- Python classes: `AccountTax`

## Field footprint

- Detected fields: 1
- Field types: `Many2one` x 1
- Relation fields: 1

## Sample fields

- `l10n_ke_tax_type_id`: `Many2one` (comodel `l10n_ke_edi_oscu.code`, compute `_compute_l10n_ke_tax_type_id`, store `True`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_l10n_ke_tax_type_id`
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
title account.tax - Direct Relations
class "account.tax" as account_tax
class "l10n_ke_edi_oscu.code" as l10n_ke_edi_oscu_code
account_tax --> l10n_ke_edi_oscu_code : l10n_ke_tax_type_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu/Models]]

<!-- GENERATED:MODEL -->
