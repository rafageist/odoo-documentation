<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# maintenance.mixin

- Module: [[docs/Community Addons/maintenance/maintenance|maintenance]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/maintenance.py`
- Python classes: `MaintenanceMixin`
- Description: Maintenance Maintained Item

## Field footprint

- Detected fields: 12
- Field types: `Date` x 3, `Integer` x 5, `Many2one` x 3, `One2many` x 1
- Relation fields: 4

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `effective_date`: `Date` (comodel `Effective Date`)
- `estimated_next_failure`: `Date` (compute `_compute_maintenance_request`)
- `expected_mtbf`: `Integer`
- `latest_failure_date`: `Date` (compute `_compute_maintenance_request`)
- `maintenance_count`: `Integer` (compute `_compute_maintenance_count`, store `True`)
- `maintenance_ids`: `One2many` (comodel `maintenance.request`)
- `maintenance_open_count`: `Integer` (compute `_compute_maintenance_count`, store `True`)
- `maintenance_team_id`: `Many2one` (comodel `maintenance.team`, compute `_compute_maintenance_team_id`, store `True`)
- `mtbf`: `Integer` (compute `_compute_maintenance_request`)
- `mttr`: `Integer` (compute `_compute_maintenance_request`)
- `technician_user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_maintenance_count`, `_compute_maintenance_request`, `_compute_maintenance_team_id`
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
title maintenance.mixin - Direct Relations
class "maintenance.mixin" as maintenance_mixin
class "maintenance.request" as maintenance_request
class "maintenance.team" as maintenance_team
class "res.company" as res_company
class "res.users" as res_users
maintenance_mixin --> res_company : company_id
maintenance_mixin --> maintenance_team : maintenance_team_id
maintenance_mixin --> res_users : technician_user_id
maintenance_mixin --|> maintenance_request : maintenance_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/maintenance/Models]]

<!-- GENERATED:MODEL -->
