<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.tax

- Module: [[docs/Enterprise Addons/l10n_ro_saft/l10n_ro_saft|l10n_ro_saft]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_tax.py`
- Python classes: `AccountTax`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Many2one` x 1
- Relation fields: 1

## Sample fields

- `l10n_ro_saft_tax_code`: `Char`
- `l10n_ro_saft_tax_type_id`: `Many2one` (comodel `l10n_ro_saft.tax.type`)

## Method hints

- Detected methods: 0
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
title account.tax - Direct Relations
class "account.tax" as account_tax
class "l10n_ro_saft.tax.type" as l10n_ro_saft_tax_type
account_tax --> l10n_ro_saft_tax_type : l10n_ro_saft_tax_type_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ro_saft/Models]]

<!-- GENERATED:MODEL -->
