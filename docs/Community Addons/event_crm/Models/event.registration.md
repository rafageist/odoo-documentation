<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# event.registration

- Module: [[docs/Community Addons/event_crm/event_crm|event_crm]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/event_registration.py`
- Python classes: `EventRegistration`

## Field footprint

- Detected fields: 2
- Field types: `Integer` x 1, `Many2many` x 1
- Relation fields: 1

## Sample fields

- `lead_count`: `Integer` (comodel `# Leads`, compute `_compute_lead_count`)
- `lead_ids`: `Many2many` (comodel `crm.lead`)

## Method hints

- Detected methods: 17
- Action methods: none
- Compute methods: `_compute_lead_count`
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
title event.registration - Direct Relations
class "event.registration" as event_registration
class "crm.lead" as crm_lead
event_registration .. crm_lead : lead_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/event_crm/Models]]

<!-- GENERATED:MODEL -->
