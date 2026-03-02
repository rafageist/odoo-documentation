<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Hr Recruitment Interview Forms

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/hr_recruitment_survey
- Dependencies: [[Odoo 19/Community Addons/survey/survey|survey]], [[Odoo 19/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]

## Summary

Surveys

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 1
- Rules (ir.rule): 14
- Access CSV entries: 15

## Detected Models

- `HrApplicant`
- `HrJob`
- `SurveySurvey`
- `SurveyUser_Input`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Hr Recruitment Interview Forms - Models and Relations
class HrApplicant
class HrJob
class SurveySurvey
class SurveyUser_Input
class "survey.survey" as survey_survey
HrApplicant --> survey_survey : many2one
class "survey.user_input" as survey_user_input
HrApplicant --|> survey_user_input : one2many
HrJob --> survey_survey : many2one
class "hr.job" as hr_job
SurveySurvey --|> hr_job : one2many
class "hr.applicant" as hr_applicant
SurveyUser_Input --> hr_applicant : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


