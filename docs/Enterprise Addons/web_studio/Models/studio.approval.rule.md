<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# studio.approval.rule

- Module: [[docs/Enterprise Addons/web_studio/web_studio|web_studio]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/studio_approval.py`
- Python classes: `StudioApprovalRule`
- Description: Studio Approval Rule
- Inherits: `mail.thread`, `studio.mixin`

## Field footprint

- Detected fields: 20
- Field types: `Boolean` x 4, `Char` x 6, `Integer` x 2, `Many2many` x 2, `Many2one` x 3, `One2many` x 2, `Selection` x 1
- Relation fields: 7

## Sample fields

- `action_id`: `Many2one` (comodel `ir.actions.actions`)
- `action_xmlid`: `Char` (related `action_id.xml_id`)
- `active`: `Boolean`
- `approval_group_id`: `Many2one` (comodel `res.groups`)
- `approver_ids`: `Many2many` (comodel `res.users`, compute `_compute_approver_ids`)
- `approver_log_ids`: `One2many` (comodel `studio.approval.rule.approver`)
- `can_validate`: `Boolean` (compute `_compute_can_validate`)
- `conditional`: `Boolean` (compute `_compute_conditional`)
- `domain`: `Char`
- `entries_count`: `Integer` (comodel `Number of Entries`, compute `_compute_entries_count`)
- `entry_ids`: `One2many` (comodel `studio.approval.entry`)
- `exclusive_user`: `Boolean`
- `kanban_color`: `Integer` (compute `_compute_kanban_color`)
- `message`: `Char`
- `method`: `Char`
- `model_id`: `Many2one` (comodel `ir.model`)
- `model_name`: `Char` (related `model_id.model`, store `True`)
- `name`: `Char`
- `notification_order`: `Selection`
- `users_to_notify`: `Many2many` (comodel `res.users`)

## Method hints

- Detected methods: 41
- Action methods: none
- Compute methods: `_compute_approver_ids`, `_compute_can_validate`, `_compute_conditional`, `_compute_display_name`, `_compute_entries_count`, `_compute_kanban_color`
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
title studio.approval.rule - Direct Relations
class "studio.approval.rule" as studio_approval_rule
class "ir.actions.actions" as ir_actions_actions
class "ir.model" as ir_model
class "res.groups" as res_groups
class "res.users" as res_users
class "studio.approval.entry" as studio_approval_entry
class "studio.approval.rule.approver" as studio_approval_rule_approver
studio_approval_rule --> ir_model : model_id
studio_approval_rule --> ir_actions_actions : action_id
studio_approval_rule .. res_users : approver_ids
studio_approval_rule --|> studio_approval_rule_approver : approver_log_ids
studio_approval_rule --> res_groups : approval_group_id
studio_approval_rule .. res_users : users_to_notify
studio_approval_rule --|> studio_approval_entry : entry_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/web_studio/Models]]

<!-- GENERATED:MODEL -->
