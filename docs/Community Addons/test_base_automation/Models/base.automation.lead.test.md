<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# base.automation.lead.test

- Module: [[docs/Community Addons/test_base_automation/test_base_automation|test_base_automation]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/test_base_automation.py`
- Python classes: `BaseAutomationLeadTest`
- Description: Automated Rule Test

## Field footprint

- Detected fields: 13
- Field types: `Boolean` x 5, `Char` x 1, `Datetime` x 1, `Many2many` x 1, `Many2one` x 3, `One2many` x 1, `Selection` x 1
- Relation fields: 5

## Sample fields

- `active`: `Boolean`
- `date_automation_last`: `Datetime`
- `deadline`: `Boolean` (compute `_compute_employee_deadline`, store `True`)
- `employee`: `Boolean` (compute `_compute_employee_deadline`, store `True`)
- `is_assigned_to_admin`: `Boolean`
- `line_ids`: `One2many` (comodel `base.automation.line.test`)
- `name`: `Char`
- `partner_id`: `Many2one` (comodel `res.partner`)
- `priority`: `Boolean`
- `stage_id`: `Many2one` (comodel `test_base_automation.stage`, compute `_compute_stage_id`, store `True`)
- `state`: `Selection`
- `tag_ids`: `Many2many` (comodel `test_base_automation.tag`)
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_employee_deadline`, `_compute_stage_id`
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
title base.automation.lead.test - Direct Relations
class "base.automation.lead.test" as base_automation_lead_test
class "base.automation.line.test" as base_automation_line_test
class "res.partner" as res_partner
class "res.users" as res_users
class "test_base_automation.stage" as test_base_automation_stage
class "test_base_automation.tag" as test_base_automation_tag
base_automation_lead_test --> res_users : user_id
base_automation_lead_test .. test_base_automation_tag : tag_ids
base_automation_lead_test --> res_partner : partner_id
base_automation_lead_test --|> base_automation_line_test : line_ids
base_automation_lead_test --> test_base_automation_stage : stage_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/test_base_automation/Models]]

<!-- GENERATED:MODEL -->
