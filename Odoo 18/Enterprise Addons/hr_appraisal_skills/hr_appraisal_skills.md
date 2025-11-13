<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Appraisal - Skills

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_appraisal_skills
- Dependencies: [[Odoo 18/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]], [[Odoo 18/Community Addons/hr_skills/hr_skills|hr_skills]]

## Summary

Manage skills of your employees during an appraisal process

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 2
- Rules (ir.rule): 2
- Access CSV entries: 3

## Detected Models

- `HrAppraisal`
- `hr.appraisal.skill`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Appraisal - Skills - Models and Relations
class HrAppraisal
class "hr.appraisal.skill" as hr_appraisal_skill
class "hr.appraisal" as hr_appraisal
hr_appraisal_skill --> hr_appraisal : many2one
class "hr.employee" as hr_employee
hr_appraisal_skill --> hr_employee : many2one
hr_appraisal_skill .. hr_employee : many2many
class "hr.skill" as hr_skill
hr_appraisal_skill --> hr_skill : many2one
class "hr.skill.level" as hr_skill_level
hr_appraisal_skill --> hr_skill_level : many2one
hr_appraisal_skill --> hr_skill_level : many2one
class "hr.skill.type" as hr_skill_type
hr_appraisal_skill --> hr_skill_type : many2one
class "hr.employee.skill" as hr_employee_skill
hr_appraisal_skill --> hr_employee_skill : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
