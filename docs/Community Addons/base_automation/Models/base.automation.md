<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# base.automation

- Module: [[docs/Community Addons/base_automation/base_automation|base_automation]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/base_automation.py`
- Python classes: `BaseAutomation`
- Description: Automation Rule
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 26
- Field types: `Boolean` x 3, `Char` x 9, `Datetime` x 1, `Html` x 1, `Integer` x 1, `Many2many` x 2, `Many2one` x 4, `Many2oneReference` x 1, `One2many` x 1, `Selection` x 3
- Relation fields: 7

## Sample fields

- `action_server_ids`: `One2many` (comodel `ir.actions.server`, compute `_compute_action_server_ids`, store `True`)
- `active`: `Boolean`
- `description`: `Html`
- `filter_domain`: `Char` (compute `_compute_filter_domain`, store `True`)
- `filter_pre_domain`: `Char` (compute `_compute_filter_pre_domain`, store `True`)
- `last_run`: `Datetime`
- `log_webhook_calls`: `Boolean`
- `model_id`: `Many2one` (comodel `ir.model`)
- `model_is_mail_thread`: `Boolean` (related `model_id.is_mail_thread`)
- `model_name`: `Char` (related `model_id.model`)
- `name`: `Char`
- `on_change_field_ids`: `Many2many` (comodel `ir.model.fields`, compute `_compute_on_change_field_ids`, store `True`)
- `previous_domain`: `Char` (store `False`)
- `record_getter`: `Char`
- `trg_date_calendar_id`: `Many2one` (comodel `resource.calendar`, compute `_compute_trg_date_calendar_id`, store `True`)
- `trg_date_id`: `Many2one` (comodel `ir.model.fields`, compute `_compute_trg_date_id`, store `True`)
- `trg_date_range`: `Integer` (compute `_compute_trg_date_range_data`, store `True`)
- `trg_date_range_mode`: `Selection` (compute `_compute_trg_date_range_data`, store `True`)
- `trg_date_range_type`: `Selection` (compute `_compute_trg_date_range_data`, store `True`)
- `trg_field_ref`: `Many2oneReference` (compute `_compute_trg_field_ref`, store `True`)

## Method hints

- Detected methods: 50
- Action methods: `action_open_scheduled_action`, `action_rotate_webhook_uuid`, `action_view_webhook_logs`
- Compute methods: `_compute_action_server_ids`, `_compute_filter_domain`, `_compute_filter_pre_domain`, `_compute_on_change_field_ids`, `_compute_trg_date_calendar_id`, `_compute_trg_date_id`, `_compute_trg_date_range_data`, `_compute_trg_field_ref`, and 5 more
- Onchange methods: `_onchange_domain`, `_onchange_trg_date_range_data`, `_onchange_trigger`, `_onchange_trigger_or_actions`

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
title base.automation - Direct Relations
class "base.automation" as base_automation
class "ir.actions.server" as ir_actions_server
class "ir.model" as ir_model
class "ir.model.fields" as ir_model_fields
class "ir.model.fields.selection" as ir_model_fields_selection
class "resource.calendar" as resource_calendar
base_automation --> ir_model : model_id
base_automation --|> ir_actions_server : action_server_ids
base_automation --> ir_model_fields_selection : trg_selection_field_id
base_automation --> ir_model_fields : trg_date_id
base_automation --> resource_calendar : trg_date_calendar_id
base_automation .. ir_model_fields : on_change_field_ids
base_automation .. ir_model_fields : trigger_field_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/base_automation/Models]]

<!-- GENERATED:MODEL -->
