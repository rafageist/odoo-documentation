<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# export.aggregator

- Module: [[docs/Community Addons/test_import_export/test_import_export|test_import_export]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/models_export.py`
- Python classes: `ExportAggregator`
- Description: Export Aggregator

## Field footprint

- Detected fields: 13
- Field types: `Boolean` x 3, `Date` x 1, `Float` x 2, `Integer` x 2, `Many2many` x 1, `Many2one` x 2, `Monetary` x 1, `One2many` x 1
- Relation fields: 4

## Sample fields

- `active`: `Boolean`
- `bool_and`: `Boolean`
- `bool_or`: `Boolean`
- `currency_id`: `Many2one` (comodel `res.currency`)
- `date_max`: `Date`
- `float_avg`: `Float`
- `float_min`: `Float`
- `float_monetary`: `Monetary`
- `int_max`: `Integer`
- `int_sum`: `Integer`
- `many2many`: `Many2many` (comodel `res.partner`)
- `many2one`: `Many2one` (comodel `export.integer`)
- `one2many`: `One2many` (comodel `export.aggregator.one2many`)

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
title export.aggregator - Direct Relations
class "export.aggregator" as export_aggregator
class "export.aggregator.one2many" as export_aggregator_one2many
class "export.integer" as export_integer
class "res.currency" as res_currency
class "res.partner" as res_partner
export_aggregator --> res_currency : currency_id
export_aggregator --> export_integer : many2one
export_aggregator --|> export_aggregator_one2many : one2many
export_aggregator .. res_partner : many2many
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/test_import_export/Models]]

<!-- GENERATED:MODEL -->
