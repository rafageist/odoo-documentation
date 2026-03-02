<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# uom.uom

- Module: [[docs/Community Addons/l10n_id_efaktur_coretax/l10n_id_efaktur_coretax|l10n_id_efaktur_coretax]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/uom_uom.py`
- Python classes: `Uom`

## Field footprint

- Detected fields: 1
- Field types: `Many2one` x 1
- Relation fields: 1

## Sample fields

- `l10n_id_uom_code`: `Many2one` (comodel `l10n_id_efaktur_coretax.uom.code`)

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
title uom.uom - Direct Relations
class "uom.uom" as uom_uom
class "l10n_id_efaktur_coretax.uom.code" as l10n_id_efaktur_coretax_uom_code
uom_uom --> l10n_id_efaktur_coretax_uom_code : l10n_id_uom_code
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_id_efaktur_coretax/Models]]

<!-- GENERATED:MODEL -->
