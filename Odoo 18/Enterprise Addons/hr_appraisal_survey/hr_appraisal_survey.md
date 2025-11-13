<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Appraisal - Survey

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_appraisal_survey
- Dependencies: [[Odoo 18/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]], [[Odoo 18/Community Addons/survey/survey|survey]]

## Summary

360 Feedback

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 1
- Rules (ir.rule): 11
- Access CSV entries: 12

## Detected Models

- `HrAppraisal`
- `hr_department`
- `ResCompany`
- `SurveySurvey`
- `SurveyUserInput`
- `SurveyQuestionAnswer`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Appraisal - Survey - Models and Relations
class HrAppraisal
class hr_department
class ResCompany
class SurveySurvey
class SurveyUserInput
class SurveyQuestionAnswer
class "hr.employee" as hr_employee
HrAppraisal .. hr_employee : many2many
class "survey.survey" as survey_survey
HrAppraisal .. survey_survey : many2many
hr_department --> survey_survey : many2one
ResCompany --> survey_survey : many2one
class "res.users" as res_users
SurveySurvey .. res_users : many2many
class "hr.appraisal" as hr_appraisal
SurveyUserInput --> hr_appraisal : many2one
SurveyQuestionAnswer --> survey_survey : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
