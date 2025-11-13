<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Skills Certification

- Version: v19
- Category: community
- Source: odoo19/addons/hr_skills_survey
- Dependencies: [[Odoo 19/Community Addons/hr_skills/hr_skills|hr_skills]], [[Odoo 19/Community Addons/survey/survey|survey]]

## Summary

Add certification to resume of your employees

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrResumeLine`
- `SurveySurvey`
- `SurveyUser_Input`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Skills Certification - Models and Relations
class HrResumeLine
class SurveySurvey
class SurveyUser_Input
class "survey.survey" as survey_survey
HrResumeLine --> survey_survey : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
