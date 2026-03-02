<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/l10n_mx_edi_extended/l10n_mx_edi_extended|l10n_mx_edi_extended]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 5
- Field types: `Char` x 4, `Many2one` x 1
- Relation fields: 1

## Sample fields

- `l10n_mx_edi_colony`: `Char` (compute `_compute_l10n_mx_edi_colony`)
- `l10n_mx_edi_colony_code`: `Char` (compute `_compute_l10n_mx_edi_colony_code`)
- `l10n_mx_edi_locality`: `Char` (compute `_compute_l10n_mx_edi_locality`)
- `l10n_mx_edi_locality_id`: `Many2one` (comodel `l10n_mx_edi.res.locality`, related `partner_id.l10n_mx_edi_locality_id`)
- `l10n_mx_edi_num_exporter`: `Char` (comodel `Number of Reliable Exporter`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_l10n_mx_edi_colony`, `_compute_l10n_mx_edi_colony_code`, `_compute_l10n_mx_edi_locality`
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
title res.company - Direct Relations
class "res.company" as res_company
class "l10n_mx_edi.res.locality" as l10n_mx_edi_res_locality
res_company --> l10n_mx_edi_res_locality : l10n_mx_edi_locality_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi_extended/Models]]

<!-- GENERATED:MODEL -->
