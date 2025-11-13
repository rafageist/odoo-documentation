<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Survey CRM

- Version: v19
- Category: community
- Source: odoo19/addons/survey_crm
- Dependencies: [[Odoo 19/Community Addons/survey/survey|survey]], [[Odoo 19/Community Addons/crm/crm|crm]]

## Summary

Generate leads from surveys

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `CrmLead`
- `CrmTeam`
- `SurveyQuestion`
- `SurveyQuestionAnswer`
- `SurveySurvey`
- `SurveyUser_Input`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Survey CRM - Models and Relations
class CrmLead
class CrmTeam
class SurveyQuestion
class SurveyQuestionAnswer
class SurveySurvey
class SurveyUser_Input
class "survey.survey" as survey_survey
CrmLead --> survey_survey : many2one
CrmTeam --|> survey_survey : one2many
class "crm.lead" as crm_lead
SurveySurvey --|> crm_lead : one2many
class "crm.team" as crm_team
SurveySurvey --> crm_team : many2one
SurveyUser_Input --> crm_lead : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
