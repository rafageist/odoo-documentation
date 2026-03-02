<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# maintenance.request

- Module: [[docs/Community Addons/maintenance/maintenance|maintenance]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/maintenance.py`
- Python classes: `MaintenanceRequest`
- Description: Maintenance Request
- Inherits: `mail.activity.mixin`, `mail.thread.cc`

## Field footprint

- Detected fields: 29
- Field types: `Binary` x 1, `Boolean` x 3, `Char` x 2, `Date` x 3, `Datetime` x 2, `Float` x 1, `Html` x 2, `Integer` x 2, `Many2one` x 7, `Selection` x 6
- Relation fields: 7

## Sample fields

- `archive`: `Boolean`
- `category_id`: `Many2one` (comodel `maintenance.equipment.category`, related `equipment_id.category_id`, store `True`)
- `close_date`: `Date` (comodel `Close Date`)
- `color`: `Integer` (comodel `Color Index`)
- `company_id`: `Many2one` (comodel `res.company`)
- `description`: `Html` (comodel `Description`)
- `done`: `Boolean` (related `stage_id.done`)
- `duration`: `Float` (compute `_compute_duration`, store `True`)
- `equipment_id`: `Many2one` (comodel `maintenance.equipment`)
- `instruction_google_slide`: `Char` (comodel `Google Slide`)
- `instruction_pdf`: `Binary` (comodel `PDF`)
- `instruction_text`: `Html` (comodel `Text`)
- `instruction_type`: `Selection`
- `kanban_state`: `Selection`
- `maintenance_team_id`: `Many2one` (comodel `maintenance.team`, compute `_compute_maintenance_team_id`, store `True`)
- `maintenance_type`: `Selection`
- `name`: `Char` (comodel `Subjects`)
- `owner_user_id`: `Many2one` (comodel `res.users`)
- `priority`: `Selection`
- `recurring_maintenance`: `Boolean` (compute `_compute_recurring_maintenance`, store `True`)

## Method hints

- Detected methods: 20
- Action methods: none
- Compute methods: `_compute_duration`, `_compute_maintenance_team_id`, `_compute_recurring_maintenance`, `_compute_schedule_end`, `_compute_user_id`
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
title maintenance.request - Direct Relations
class "maintenance.request" as maintenance_request
class "maintenance.equipment" as maintenance_equipment
class "maintenance.equipment.category" as maintenance_equipment_category
class "maintenance.stage" as maintenance_stage
class "maintenance.team" as maintenance_team
class "res.company" as res_company
class "res.users" as res_users
maintenance_request --> res_company : company_id
maintenance_request --> res_users : owner_user_id
maintenance_request --> maintenance_equipment_category : category_id
maintenance_request --> maintenance_equipment : equipment_id
maintenance_request --> res_users : user_id
maintenance_request --> maintenance_stage : stage_id
maintenance_request --> maintenance_team : maintenance_team_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/maintenance/Models]]

<!-- GENERATED:MODEL -->
