<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Appraisal - Skills

- Scope: Enterprise Addons
- Source: enterprise/hr_appraisal_skills
- Dependencies: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]], [[docs/Community Addons/hr_skills/hr_skills|hr_skills]]

## Summary

Manage skills of your employees during an appraisal process

## XML Artifacts (detected)

- Views: 14
- Actions: 2
- Menus: 2
- Rules (ir.rule): 5
- Access CSV entries: 4

## Detected Models

- `HrAppraisal`
- `HrAppraisalGoal`
- `hr.appraisal.goal.skill`
- `hr.appraisal.skill`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Appraisal - Skills - Models and Relations
class HrAppraisal
class HrAppraisalGoal
class "hr.appraisal.goal.skill" as hr_appraisal_goal_skill
class "hr.appraisal.skill" as hr_appraisal_skill
class "hr.job" as hr_job
HrAppraisal --> hr_job : many2one
HrAppraisal --|> hr_appraisal_skill : one2many
HrAppraisal --|> hr_appraisal_skill : one2many
HrAppraisalGoal --|> hr_appraisal_goal_skill : one2many
HrAppraisalGoal --|> hr_appraisal_goal_skill : one2many
class "hr.appraisal.goal" as hr_appraisal_goal
hr_appraisal_goal_skill --> hr_appraisal_goal : many2one
class "hr.appraisal" as hr_appraisal
hr_appraisal_skill --> hr_appraisal : many2one
class "hr.skill.level" as hr_skill_level
hr_appraisal_skill --> hr_skill_level : many2one
hr_appraisal_skill --> hr_skill_level : many2one
class "hr.employee" as hr_employee
hr_appraisal_skill .. hr_employee : many2many
hr_appraisal_skill .. hr_appraisal_goal : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




