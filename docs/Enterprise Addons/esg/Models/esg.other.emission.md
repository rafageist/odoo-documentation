<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# esg.other.emission

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/esg_other_emission.py`
- Python classes: `EsgOtherEmission`
- Description: Other Emission

## Field footprint

- Detected fields: 14
- Field types: `Char` x 1, `Date` x 2, `Float` x 4, `Integer` x 1, `Many2one` x 4, `Selection` x 1, `Text` x 1
- Relation fields: 4

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `compute_method`: `Selection` (related `esg_emission_factor_id.compute_method`)
- `currency_id`: `Many2one` (comodel `res.currency`, compute `_compute_currency_id`, store `True`)
- `date`: `Date`
- `date_end`: `Date`
- `esg_emission_factor_id`: `Many2one` (comodel `esg.emission.factor`)
- `esg_emission_multiplicator`: `Float` (compute `_compute_esg_emission_multiplicator`, store `True`)
- `esg_emissions_value`: `Float` (compute `_compute_esg_emissions_value`)
- `esg_uncertainty_absolute_value`: `Float` (compute `_compute_esg_uncertainty_absolute_value`)
- `esg_uncertainty_value`: `Float` (related `esg_emission_factor_id.esg_uncertainty_value`)
- `name`: `Char`
- `note`: `Text`
- `quantity`: `Integer`
- `uom_id`: `Many2one` (comodel `uom.uom`, compute `_compute_uom_id`, store `True`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_currency_id`, `_compute_esg_emission_multiplicator`, `_compute_esg_emissions_value`, `_compute_esg_uncertainty_absolute_value`, `_compute_uom_id`
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
title esg.other.emission - Direct Relations
class "esg.other.emission" as esg_other_emission
class "esg.emission.factor" as esg_emission_factor
class "res.company" as res_company
class "res.currency" as res_currency
class "uom.uom" as uom_uom
esg_other_emission --> res_company : company_id
esg_other_emission --> esg_emission_factor : esg_emission_factor_id
esg_other_emission --> uom_uom : uom_id
esg_other_emission --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Models]]

<!-- GENERATED:MODEL -->
