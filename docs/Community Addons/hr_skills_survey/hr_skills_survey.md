<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Skills Certification

- Scope: Community Addons
- Source: odoo/addons/hr_skills_survey
- Dependencies: [[docs/Community Addons/hr_skills/hr_skills|hr_skills]], [[docs/Community Addons/survey/survey|survey]]

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
!include ../../../templates/DiagramStyles.puml
title Skills Certification - Models and Relations
class HrResumeLine
class SurveySurvey
class SurveyUser_Input
class "survey.survey" as survey_survey
HrResumeLine --> survey_survey : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





