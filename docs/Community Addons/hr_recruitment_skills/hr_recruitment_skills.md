<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Recruitment - Skills Management

- Scope: Community Addons
- Source: odoo/addons/hr_recruitment_skills
- Dependencies: [[docs/Community Addons/hr_skills/hr_skills|hr_skills]], [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]

## Summary

Manage skills of your employees

## XML Artifacts (detected)

- Views: 8
- Actions: 2
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `HrApplicant`
- `hr.applicant.skill`
- `HrJob`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Recruitment - Skills Management - Models and Relations
class HrApplicant
class "hr.applicant.skill" as hr_applicant_skill
class HrJob
HrApplicant --|> hr_applicant_skill : one2many
HrApplicant --|> hr_applicant_skill : one2many
class "hr.skill" as hr_skill
HrApplicant .. hr_skill : many2many
HrApplicant .. hr_skill : many2many
HrApplicant .. hr_skill : many2many
class "hr.applicant" as hr_applicant
hr_applicant_skill --> hr_applicant : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





