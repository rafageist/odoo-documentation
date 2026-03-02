<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Recruitment - Skills Management

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/hr_recruitment_skills
- Dependencies: [[Odoo 19/Community Addons/hr_skills/hr_skills|hr_skills]], [[Odoo 19/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


