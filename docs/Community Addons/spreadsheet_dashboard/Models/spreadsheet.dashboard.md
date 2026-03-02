<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# spreadsheet.dashboard

- Module: [[docs/Community Addons/spreadsheet_dashboard/spreadsheet_dashboard|spreadsheet_dashboard]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/spreadsheet_dashboard.py`
- Python classes: `SpreadsheetDashboard`
- Description: Spreadsheet Dashboard
- Inherits: `spreadsheet.mixin`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 2, `Char` x 2, `Integer` x 1, `Many2many` x 4, `Many2one` x 1
- Relation fields: 5

## Sample fields

- `company_ids`: `Many2many` (comodel `res.company`)
- `dashboard_group_id`: `Many2one` (comodel `spreadsheet.dashboard.group`)
- `favorite_user_ids`: `Many2many` (comodel `res.users`)
- `group_ids`: `Many2many` (comodel `res.groups`)
- `is_favorite`: `Boolean` (compute `_compute_is_favorite`)
- `is_published`: `Boolean`
- `main_data_model_ids`: `Many2many` (comodel `ir.model`)
- `name`: `Char`
- `sample_dashboard_file_path`: `Char`
- `sequence`: `Integer`

## Method hints

- Detected methods: 7
- Action methods: `action_toggle_favorite`
- Compute methods: `_compute_is_favorite`
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
title spreadsheet.dashboard - Direct Relations
class "spreadsheet.dashboard" as spreadsheet_dashboard
class "ir.model" as ir_model
class "res.company" as res_company
class "res.groups" as res_groups
class "res.users" as res_users
class "spreadsheet.dashboard.group" as spreadsheet_dashboard_group
spreadsheet_dashboard --> spreadsheet_dashboard_group : dashboard_group_id
spreadsheet_dashboard .. res_company : company_ids
spreadsheet_dashboard .. res_groups : group_ids
spreadsheet_dashboard .. res_users : favorite_user_ids
spreadsheet_dashboard .. ir_model : main_data_model_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/spreadsheet_dashboard/Models]]

<!-- GENERATED:MODEL -->
