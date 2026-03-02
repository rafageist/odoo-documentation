<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# onboarding.progress

- Module: [[docs/Community Addons/onboarding/onboarding|onboarding]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/onboarding_progress.py`
- Python classes: `OnboardingProgress`
- Description: Onboarding Progress Tracker

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Many2many` x 1, `Many2one` x 2, `Selection` x 1
- Relation fields: 3

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `is_onboarding_closed`: `Boolean` (comodel `Was panel closed?`)
- `onboarding_id`: `Many2one` (comodel `onboarding.onboarding`)
- `onboarding_state`: `Selection` (compute `_compute_onboarding_state`, store `True`)
- `progress_step_ids`: `Many2many` (comodel `onboarding.progress.step`)

## Method hints

- Detected methods: 5
- Action methods: `action_close`, `action_toggle_visibility`
- Compute methods: `_compute_onboarding_state`
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
title onboarding.progress - Direct Relations
class "onboarding.progress" as onboarding_progress
class "onboarding.onboarding" as onboarding_onboarding
class "onboarding.progress.step" as onboarding_progress_step
class "res.company" as res_company
onboarding_progress --> res_company : company_id
onboarding_progress --> onboarding_onboarding : onboarding_id
onboarding_progress .. onboarding_progress_step : progress_step_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/onboarding/Models]]

<!-- GENERATED:MODEL -->
