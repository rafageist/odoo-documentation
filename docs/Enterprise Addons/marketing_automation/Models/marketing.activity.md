<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# marketing.activity

- Module: [[docs/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/marketing_activity.py`
- Python classes: `MarketingActivity`
- Description: Marketing Activity
- Inherits: `utm.source.mixin`

## Field footprint

- Detected fields: 32
- Field types: `Boolean` x 2, `Char` x 4, `Html` x 1, `Integer` x 10, `Many2many` x 1, `Many2one` x 6, `One2many` x 2, `Selection` x 6
- Relation fields: 9

## Sample fields

- `activity_domain`: `Char`
- `activity_summary`: `Html` (compute `_compute_activity_summary`)
- `activity_type`: `Selection`
- `allowed_parent_ids`: `Many2many` (comodel `marketing.activity`, compute `_compute_allowed_parent_ids`)
- `campaign_id`: `Many2one` (comodel `marketing.campaign`)
- `child_ids`: `One2many` (comodel `marketing.activity`)
- `domain`: `Char` (compute `_compute_inherited_domain`, store `True`)
- `interval_number`: `Integer`
- `interval_standardized`: `Integer` (comodel `Send after (in hours)`, compute `_compute_interval_standardized`, store `True`)
- `interval_type`: `Selection`
- `mass_mailing_id`: `Many2one` (comodel `mailing.mailing`, compute `_compute_mass_mailing_id`, store `True`)
- `mass_mailing_id_mailing_type`: `Selection` (compute `_compute_mass_mailing_id_mailing_type`, store `True`)
- `model_id`: `Many2one` (comodel `ir.model`, related `campaign_id.model_id`)
- `model_name`: `Char` (related `model_id.model`)
- `parent_id`: `Many2one` (comodel `marketing.activity`, compute `_compute_parent_id`, store `True`)
- `processed`: `Integer` (compute `_compute_statistics`)
- `rejected`: `Integer` (compute `_compute_statistics`)
- `require_sync`: `Boolean` (comodel `Require trace sync`)
- `server_action_id`: `Many2one` (comodel `ir.actions.server`, compute `_compute_server_action_id`, store `True`)
- `statistics_graph_data`: `Char` (compute `_compute_statistics_graph_data`)

## Method hints

- Detected methods: 30
- Action methods: `action_view_clicked`, `action_view_opened`, `action_view_replied`, `action_view_sent`
- Compute methods: `_compute_activity_summary`, `_compute_allowed_parent_ids`, `_compute_inherited_domain`, `_compute_interval_standardized`, `_compute_mass_mailing_id`, `_compute_mass_mailing_id_mailing_type`, `_compute_parent_id`, `_compute_server_action_id`, and 3 more
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
title marketing.activity - Direct Relations
class "marketing.activity" as marketing_activity
class "ir.actions.server" as ir_actions_server
class "ir.model" as ir_model
class "mailing.mailing" as mailing_mailing
class "marketing.activity" as marketing_activity
class "marketing.campaign" as marketing_campaign
class "marketing.trace" as marketing_trace
class "utm.campaign" as utm_campaign
marketing_activity --> mailing_mailing : mass_mailing_id
marketing_activity --> ir_actions_server : server_action_id
marketing_activity --> marketing_campaign : campaign_id
marketing_activity --> utm_campaign : utm_campaign_id
marketing_activity --> ir_model : model_id
marketing_activity --> marketing_activity : parent_id
marketing_activity .. marketing_activity : allowed_parent_ids
marketing_activity --|> marketing_activity : child_ids
marketing_activity --|> marketing_trace : trace_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/marketing_automation/Models]]

<!-- GENERATED:MODEL -->
