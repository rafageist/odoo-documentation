<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# survey.user_input

- Module: [[docs/Community Addons/website_slides_survey/website_slides_survey|website_slides_survey]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/survey_user.py`
- Python classes: `SurveyUser_Input`

## Field footprint

- Detected fields: 2
- Field types: `Many2one` x 2
- Relation fields: 2

## Sample fields

- `slide_id`: `Many2one` (comodel `slide.slide`)
- `slide_partner_id`: `Many2one` (comodel `slide.slide.partner`)

## Method hints

- Detected methods: 3
- Action methods: none
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
title survey.user_input - Direct Relations
class "survey.user_input" as survey_user_input
class "slide.slide" as slide_slide
class "slide.slide.partner" as slide_slide_partner
survey_user_input --> slide_slide : slide_id
survey_user_input --> slide_slide_partner : slide_partner_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_slides_survey/Models]]

<!-- GENERATED:MODEL -->
