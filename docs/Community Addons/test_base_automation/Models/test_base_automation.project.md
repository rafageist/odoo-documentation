<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# test_base_automation.project

- Module: [[docs/Community Addons/test_base_automation/test_base_automation|test_base_automation]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/test_base_automation.py`
- Python classes: `Test_Base_AutomationProject`
- Description: test_base_automation.project

## Field footprint

- Detected fields: 6
- Field types: `Char` x 1, `Many2many` x 2, `Many2one` x 1, `One2many` x 1, `Selection` x 1
- Relation fields: 4

## Sample fields

- `name`: `Char`
- `priority`: `Selection`
- `stage_id`: `Many2one` (comodel `test_base_automation.stage`)
- `tag_ids`: `Many2many` (comodel `test_base_automation.tag`)
- `task_ids`: `One2many` (comodel `test_base_automation.task`)
- `user_ids`: `Many2many` (comodel `res.users`)

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
title test_base_automation.project - Direct Relations
class "test_base_automation.project" as test_base_automation_project
class "res.users" as res_users
class "test_base_automation.stage" as test_base_automation_stage
class "test_base_automation.tag" as test_base_automation_tag
class "test_base_automation.task" as test_base_automation_task
test_base_automation_project --|> test_base_automation_task : task_ids
test_base_automation_project --> test_base_automation_stage : stage_id
test_base_automation_project .. test_base_automation_tag : tag_ids
test_base_automation_project .. res_users : user_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/test_base_automation/Models]]

<!-- GENERATED:MODEL -->
