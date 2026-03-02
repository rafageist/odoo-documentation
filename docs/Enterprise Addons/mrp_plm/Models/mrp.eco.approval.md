<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# mrp.eco.approval

- Module: [[docs/Enterprise Addons/mrp_plm/mrp_plm|mrp_plm]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/mrp_eco.py`
- Python classes: `MrpEcoApproval`
- Description: ECO Approval

## Field footprint

- Detected fields: 13
- Field types: `Boolean` x 4, `Char` x 1, `Datetime` x 1, `Many2many` x 1, `Many2one` x 5, `Selection` x 1
- Relation fields: 6

## Sample fields

- `approval_date`: `Datetime` (comodel `Approval Date`)
- `approval_template_id`: `Many2one` (comodel `mrp.eco.approval.template`)
- `awaiting_my_validation`: `Boolean` (compute `_compute_awaiting_my_validation`)
- `eco_id`: `Many2one` (comodel `mrp.eco`)
- `eco_stage_id`: `Many2one` (comodel `mrp.eco.stage`, related `eco_id.stage_id`)
- `is_approved`: `Boolean` (compute `_compute_is_approved`, store `True`)
- `is_closed`: `Boolean`
- `is_rejected`: `Boolean` (compute `_compute_is_rejected`, store `True`)
- `name`: `Char` (comodel `Role`, related `approval_template_id.name`)
- `required_user_ids`: `Many2many` (comodel `res.users`, related `approval_template_id.user_ids`)
- `status`: `Selection`
- `template_stage_id`: `Many2one` (comodel `mrp.eco.stage`, related `approval_template_id.stage_id`)
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_awaiting_my_validation`, `_compute_is_approved`, `_compute_is_rejected`
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
title mrp.eco.approval - Direct Relations
class "mrp.eco.approval" as mrp_eco_approval
class "mrp.eco" as mrp_eco
class "mrp.eco.approval.template" as mrp_eco_approval_template
class "mrp.eco.stage" as mrp_eco_stage
class "res.users" as res_users
mrp_eco_approval --> mrp_eco : eco_id
mrp_eco_approval --> mrp_eco_approval_template : approval_template_id
mrp_eco_approval --> res_users : user_id
mrp_eco_approval .. res_users : required_user_ids
mrp_eco_approval --> mrp_eco_stage : template_stage_id
mrp_eco_approval --> mrp_eco_stage : eco_stage_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_plm/Models]]

<!-- GENERATED:MODEL -->
