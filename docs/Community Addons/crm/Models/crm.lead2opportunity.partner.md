<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# crm.lead2opportunity.partner

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/crm_lead_to_opportunity.py`
- Python classes: `CrmLead2opportunityPartner`
- Description: Convert Lead to Opportunity (not in mass)

## Field footprint

- Detected fields: 11
- Field types: `Boolean` x 1, `Char` x 2, `Many2many` x 1, `Many2one` x 5, `Selection` x 2
- Relation fields: 6

## Sample fields

- `action`: `Selection` (compute `_compute_action`, store `True`)
- `commercial_partner_id`: `Many2one` (comodel `res.partner`, compute `_compute_commercial_partner_id`, store `True`)
- `duplicated_lead_ids`: `Many2many` (comodel `crm.lead`, compute `_compute_duplicated_lead_ids`, store `True`)
- `force_assignment`: `Boolean` (comodel `Force assignment`)
- `lead_contact_name`: `Char` (related `lead_id.contact_name`)
- `lead_id`: `Many2one` (comodel `crm.lead`)
- `lead_partner_name`: `Char` (related `lead_id.partner_name`)
- `name`: `Selection` (compute `_compute_name`, store `True`)
- `partner_id`: `Many2one` (comodel `res.partner`, compute `_compute_partner_id`, store `True`)
- `team_id`: `Many2one` (comodel `crm.team`, compute `_compute_team_id`, store `True`)
- `user_id`: `Many2one` (comodel `res.users`, compute `_compute_user_id`, store `True`)

## Method hints

- Detected methods: 13
- Action methods: `action_apply`
- Compute methods: `_compute_action`, `_compute_commercial_partner_id`, `_compute_duplicated_lead_ids`, `_compute_name`, `_compute_partner_id`, `_compute_team_id`, `_compute_user_id`
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
title crm.lead2opportunity.partner - Direct Relations
class "crm.lead2opportunity.partner" as crm_lead2opportunity_partner
class "crm.lead" as crm_lead
class "crm.team" as crm_team
class "res.partner" as res_partner
class "res.users" as res_users
crm_lead2opportunity_partner --> crm_lead : lead_id
crm_lead2opportunity_partner .. crm_lead : duplicated_lead_ids
crm_lead2opportunity_partner --> res_partner : commercial_partner_id
crm_lead2opportunity_partner --> res_partner : partner_id
crm_lead2opportunity_partner --> res_users : user_id
crm_lead2opportunity_partner --> crm_team : team_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/crm/Models]]

<!-- GENERATED:MODEL -->
