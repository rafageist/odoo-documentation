<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# onboarding.progress.step

- Module: [[docs/Community Addons/onboarding/onboarding|onboarding]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/onboarding_progress_step.py`
- Python classes: `OnboardingProgressStep`
- Description: Onboarding Progress Step Tracker

## Field footprint

- Detected fields: 4
- Field types: `Many2many` x 1, `Many2one` x 2, `Selection` x 1
- Relation fields: 3

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `progress_ids`: `Many2many` (comodel `onboarding.progress`)
- `step_id`: `Many2one` (comodel `onboarding.onboarding.step`)
- `step_state`: `Selection`

## Method hints

- Detected methods: 2
- Action methods: `action_consolidate_just_done`, `action_set_just_done`
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
title onboarding.progress.step - Direct Relations
class "onboarding.progress.step" as onboarding_progress_step
class "onboarding.onboarding.step" as onboarding_onboarding_step
class "onboarding.progress" as onboarding_progress
class "res.company" as res_company
onboarding_progress_step .. onboarding_progress : progress_ids
onboarding_progress_step --> onboarding_onboarding_step : step_id
onboarding_progress_step --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/onboarding/Models]]

<!-- GENERATED:MODEL -->
