<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Appraisal - Survey

- Scope: Enterprise Addons
- Source: enterprise/hr_appraisal_survey
- Dependencies: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]], [[docs/Community Addons/survey/survey|survey]]

## Summary

360 Feedback

## XML Artifacts (detected)

- Views: 9
- Actions: 2
- Menus: 1
- Rules (ir.rule): 11
- Access CSV entries: 13

## Detected Models

- `HrAppraisal`
- `HrAppraisalTemplate`
- `SurveySurvey`
- `SurveyUser_Input`
- `SurveyQuestionAnswer`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Appraisal - Survey - Models and Relations
class HrAppraisal
class HrAppraisalTemplate
class SurveySurvey
class SurveyUser_Input
class SurveyQuestionAnswer
class "hr.employee" as hr_employee
HrAppraisal .. hr_employee : many2many
class "survey.survey" as survey_survey
HrAppraisal .. survey_survey : many2many
HrAppraisalTemplate .. survey_survey : many2many
class "res.users" as res_users
SurveySurvey .. res_users : many2many
class "hr.appraisal" as hr_appraisal
SurveyUser_Input --> hr_appraisal : many2one
SurveyQuestionAnswer --> survey_survey : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



