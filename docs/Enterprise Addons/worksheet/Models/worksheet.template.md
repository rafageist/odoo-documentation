<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# worksheet.template

- Module: [[docs/Enterprise Addons/worksheet/worksheet|worksheet]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/worksheet_template.py`
- Python classes: `WorksheetTemplate`
- Description: Worksheet Template

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Char` x 2, `Integer` x 2, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `action_id`: `Many2one` (comodel `ir.actions.act_window`)
- `active`: `Boolean`
- `company_id`: `Many2one` (comodel `res.company`)
- `model_id`: `Many2one` (comodel `ir.model`)
- `name`: `Char`
- `report_view_id`: `Many2one` (comodel `ir.ui.view`)
- `res_model`: `Char` (comodel `Host Model`)
- `sequence`: `Integer`
- `worksheet_count`: `Integer` (compute `_compute_worksheet_count`)

## Method hints

- Detected methods: 22
- Action methods: `action_analysis_report`, `action_view_worksheets`
- Compute methods: `_compute_worksheet_count`
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
title worksheet.template - Direct Relations
class "worksheet.template" as worksheet_template
class "ir.actions.act_window" as ir_actions_act_window
class "ir.model" as ir_model
class "ir.ui.view" as ir_ui_view
class "res.company" as res_company
worksheet_template --> ir_model : model_id
worksheet_template --> ir_actions_act_window : action_id
worksheet_template --> res_company : company_id
worksheet_template --> ir_ui_view : report_view_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/worksheet/Models]]

<!-- GENERATED:MODEL -->
