<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Skills Certification

- Version: v18
- Category: community
- Source: odoo/addons/hr_skills_survey
- Dependencies: [[Odoo 18/Community Addons/hr_skills/hr_skills|hr_skills]], [[Odoo 18/Community Addons/survey/survey|survey]]

## Summary

Add certification to resume of your employees

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ResumeLine`
- `SurveySurvey`
- `SurveyUserInput`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Skills Certification - Models and Relations
class ResumeLine
class SurveySurvey
class SurveyUserInput
class "survey.survey" as survey_survey
ResumeLine --> survey_survey : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
