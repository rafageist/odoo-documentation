<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Recruitment - Skills Management

- Version: v18
- Category: community
- Source: odoo/addons/hr_recruitment_skills
- Dependencies: [[Odoo 18/Community Addons/hr_skills/hr_skills|hr_skills]], [[Odoo 18/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]

## Summary

Manage skills of your employees

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 1

## Detected Models

- `HrApplicant`
- `HrCandidate`
- `hr.candidate.skill`
- `HrJob`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Recruitment - Skills Management - Models and Relations
class HrApplicant
class HrCandidate
class "hr.candidate.skill" as hr_candidate_skill
class HrJob
HrCandidate --|> hr_candidate_skill : one2many
class "hr.skill" as hr_skill
HrCandidate .. hr_skill : many2many
HrCandidate .. hr_skill : many2many
HrCandidate .. hr_skill : many2many
class "hr.candidate" as hr_candidate
hr_candidate_skill --> hr_candidate : many2one
hr_candidate_skill --> hr_skill : many2one
class "hr.skill.level" as hr_skill_level
hr_candidate_skill --> hr_skill_level : many2one
class "hr.skill.type" as hr_skill_type
hr_candidate_skill --> hr_skill_type : many2one
HrJob .. hr_skill : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
