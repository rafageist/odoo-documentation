<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# data_recycle.model

- Module: [[docs/Community Addons/data_recycle/data_recycle|data_recycle]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/data_recycle_model.py`
- Python classes: `Data_RecycleModel`
- Description: Recycling Model

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 2, `Char` x 3, `Datetime` x 1, `Integer` x 3, `Many2many` x 1, `Many2one` x 2, `One2many` x 1, `Selection` x 4
- Relation fields: 4

## Sample fields

- `active`: `Boolean`
- `domain`: `Char` (compute `_compute_domain`, store `True`)
- `include_archived`: `Boolean`
- `last_notification`: `Datetime`
- `name`: `Char` (compute `_compute_name`, store `True`)
- `notify_frequency`: `Integer`
- `notify_frequency_period`: `Selection`
- `notify_user_ids`: `Many2many` (comodel `res.users`)
- `records_to_recycle_count`: `Integer` (comodel `Records To Recycle`, compute `_compute_records_to_recycle_count`)
- `recycle_action`: `Selection`
- `recycle_mode`: `Selection`
- `recycle_record_ids`: `One2many` (comodel `data_recycle.record`)
- `res_model_id`: `Many2one` (comodel `ir.model`)
- `res_model_name`: `Char` (related `res_model_id.model`, store `True`)
- `time_field_delta`: `Integer`
- `time_field_delta_unit`: `Selection`
- `time_field_id`: `Many2one` (comodel `ir.model.fields`)

## Method hints

- Detected methods: 11
- Action methods: `action_recycle_records`
- Compute methods: `_compute_domain`, `_compute_name`, `_compute_records_to_recycle_count`
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
title data_recycle.model - Direct Relations
class "data_recycle.model" as data_recycle_model
class "data_recycle.record" as data_recycle_record
class "ir.model" as ir_model
class "ir.model.fields" as ir_model_fields
class "res.users" as res_users
data_recycle_model --> ir_model : res_model_id
data_recycle_model --|> data_recycle_record : recycle_record_ids
data_recycle_model --> ir_model_fields : time_field_id
data_recycle_model .. res_users : notify_user_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/data_recycle/Models]]

<!-- GENERATED:MODEL -->
