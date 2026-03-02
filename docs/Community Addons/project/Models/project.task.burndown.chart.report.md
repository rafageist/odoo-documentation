<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# project.task.burndown.chart.report

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `report/project_task_burndown_chart_report.py`
- Python classes: `ProjectTaskBurndownChartReport`
- Description: Burndown Chart

## Field footprint

- Detected fields: 13
- Field types: `Date` x 2, `Datetime` x 2, `Float` x 1, `Many2many` x 2, `Many2one` x 4, `Selection` x 2
- Relation fields: 6

## Sample fields

- `allocated_hours`: `Float`
- `date`: `Datetime` (comodel `Date`)
- `date_assign`: `Datetime`
- `date_deadline`: `Date`
- `date_last_stage_update`: `Date`
- `is_closed`: `Selection`
- `milestone_id`: `Many2one` (comodel `project.milestone`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `project_id`: `Many2one` (comodel `project.project`)
- `stage_id`: `Many2one` (comodel `project.task.type`)
- `state`: `Selection`
- `tag_ids`: `Many2many` (comodel `project.tags`)
- `user_ids`: `Many2many` (comodel `res.users`)

## Method hints

- Detected methods: 6
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
title project.task.burndown.chart.report - Direct Relations
class "project.task.burndown.chart.report" as project_task_burndown_chart_report
class "project.milestone" as project_milestone
class "project.project" as project_project
class "project.tags" as project_tags
class "project.task.type" as project_task_type
class "res.partner" as res_partner
class "res.users" as res_users
project_task_burndown_chart_report --> project_milestone : milestone_id
project_task_burndown_chart_report --> res_partner : partner_id
project_task_burndown_chart_report --> project_project : project_id
project_task_burndown_chart_report --> project_task_type : stage_id
project_task_burndown_chart_report .. project_tags : tag_ids
project_task_burndown_chart_report .. res_users : user_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/project/Models]]

<!-- GENERATED:MODEL -->
