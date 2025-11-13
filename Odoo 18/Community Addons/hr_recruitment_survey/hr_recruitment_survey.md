<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Hr Recruitment Interview Forms

- Version: v18
- Category: community
- Source: odoo/addons/hr_recruitment_survey
- Dependencies: [[Odoo 18/Community Addons/survey/survey|survey]], [[Odoo 18/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]

## Summary

Surveys

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 1
- Rules (ir.rule): 14
- Access CSV entries: 15

## Detected Models

- `Applicant`
- `Job`
- `SurveySurvey`
- `SurveyUserInput`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Hr Recruitment Interview Forms - Models and Relations
class Applicant
class Job
class SurveySurvey
class SurveyUserInput
class "survey.survey" as survey_survey
Applicant --> survey_survey : many2one
class "survey.user_input" as survey_user_input
Applicant --|> survey_user_input : one2many
Job --> survey_survey : many2one
class "hr.job" as hr_job
SurveySurvey --|> hr_job : one2many
class "hr.applicant" as hr_applicant
SurveyUserInput --> hr_applicant : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
