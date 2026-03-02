<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# maintenance.equipment

- Module: [[docs/Community Addons/maintenance/maintenance|maintenance]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/maintenance.py`
- Python classes: `MaintenanceEquipment`
- Description: Maintenance Equipment
- Inherits: `mail.activity.mixin`, `mail.thread`, `maintenance.mixin`

## Field footprint

- Detected fields: 16
- Field types: `Boolean` x 1, `Char` x 4, `Date` x 3, `Float` x 1, `Html` x 1, `Integer` x 1, `Many2one` x 3, `One2many` x 1, `Properties` x 1
- Relation fields: 4

## Sample fields

- `active`: `Boolean`
- `assign_date`: `Date` (comodel `Assigned Date`)
- `category_id`: `Many2one` (comodel `maintenance.equipment.category`)
- `color`: `Integer` (comodel `Color Index`)
- `cost`: `Float` (comodel `Cost`)
- `equipment_properties`: `Properties` (comodel `Properties`)
- `maintenance_ids`: `One2many` (comodel `maintenance.request`)
- `model`: `Char` (comodel `Model`)
- `name`: `Char` (comodel `Equipment Name`)
- `note`: `Html` (comodel `Note`)
- `owner_user_id`: `Many2one` (comodel `res.users`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `partner_ref`: `Char` (comodel `Vendor Reference`)
- `scrap_date`: `Date` (comodel `Scrap Date`)
- `serial_no`: `Char` (comodel `Serial Number`)
- `warranty_date`: `Date` (comodel `Warranty Expiration Date`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_display_name`
- Onchange methods: `_onchange_category_id`

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
title maintenance.equipment - Direct Relations
class "maintenance.equipment" as maintenance_equipment
class "maintenance.equipment.category" as maintenance_equipment_category
class "maintenance.request" as maintenance_request
class "res.partner" as res_partner
class "res.users" as res_users
maintenance_equipment --> res_users : owner_user_id
maintenance_equipment --> maintenance_equipment_category : category_id
maintenance_equipment --> res_partner : partner_id
maintenance_equipment --|> maintenance_request : maintenance_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/maintenance/Models]]

<!-- GENERATED:MODEL -->
