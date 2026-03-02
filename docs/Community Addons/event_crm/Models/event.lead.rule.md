<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# event.lead.rule

- Module: [[docs/Community Addons/event_crm/event_crm|event_crm]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/event_lead_rule.py`
- Python classes: `EventLeadRule`
- Description: Event Lead Rules

## Field footprint

- Detected fields: 13
- Field types: `Boolean` x 1, `Char` x 1, `Many2many` x 2, `Many2one` x 4, `One2many` x 1, `Selection` x 3, `Text` x 1
- Relation fields: 7

## Sample fields

- `active`: `Boolean` (comodel `Active`)
- `company_id`: `Many2one` (comodel `res.company`)
- `event_id`: `Many2one` (comodel `event.event`)
- `event_registration_filter`: `Text`
- `event_type_ids`: `Many2many` (comodel `event.type`)
- `lead_creation_basis`: `Selection`
- `lead_creation_trigger`: `Selection`
- `lead_ids`: `One2many` (comodel `crm.lead`)
- `lead_sales_team_id`: `Many2one` (comodel `crm.team`)
- `lead_tag_ids`: `Many2many` (comodel `crm.tag`)
- `lead_type`: `Selection`
- `lead_user_id`: `Many2one` (comodel `res.users`)
- `name`: `Char` (comodel `Rule Name`)

## Method hints

- Detected methods: 4
- Action methods: `action_execute_rule`
- Compute methods: none
- Onchange methods: `_onchange_lead_sales_team_id`

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
title event.lead.rule - Direct Relations
class "event.lead.rule" as event_lead_rule
class "crm.lead" as crm_lead
class "crm.tag" as crm_tag
class "crm.team" as crm_team
class "event.event" as event_event
class "event.type" as event_type
class "res.company" as res_company
class "res.users" as res_users
event_lead_rule --|> crm_lead : lead_ids
event_lead_rule .. event_type : event_type_ids
event_lead_rule --> event_event : event_id
event_lead_rule --> res_company : company_id
event_lead_rule --> crm_team : lead_sales_team_id
event_lead_rule --> res_users : lead_user_id
event_lead_rule .. crm_tag : lead_tag_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/event_crm/Models]]

<!-- GENERATED:MODEL -->
