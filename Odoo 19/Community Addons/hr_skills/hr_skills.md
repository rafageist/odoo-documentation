<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Skills Management

- Version: v19
- Category: community
- Source: odoo19/addons/hr_skills
- Dependencies: [[Odoo 19/Community Addons/hr/hr|hr]]

## Summary

Manage skills, knowledge and resume of your employees

## XML Artifacts (detected)

- Views: 36
- Actions: 11
- Menus: 9
- Rules (ir.rule): 11
- Access CSV entries: 20

## Detected Models

- `HrEmployee`
- `HrEmployeePublic`
- `hr.employee.skill`
- `HrJob`
- `hr.job.skill`
- `hr.resume.line`
- `hr.resume.line.type`
- `hr.skill`
- `hr.skill.level`
- `hr.skill.type`
- `ResourceResource`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Skills Management - Models and Relations
class HrEmployee
class HrEmployeePublic
class "hr.employee.skill" as hr_employee_skill
class HrJob
class "hr.job.skill" as hr_job_skill
class "hr.resume.line" as hr_resume_line
class "hr.resume.line.type" as hr_resume_line_type
class "hr.skill" as hr_skill
class "hr.skill.level" as hr_skill_level
class "hr.skill.type" as hr_skill_type
class ResourceResource
HrEmployee --|> hr_resume_line : one2many
HrEmployee --|> hr_employee_skill : one2many
HrEmployee --|> hr_employee_skill : one2many
HrEmployee .. hr_skill : many2many
HrEmployee --|> hr_employee_skill : one2many
HrEmployeePublic --|> hr_resume_line : one2many
HrEmployeePublic --|> hr_employee_skill : one2many
HrEmployeePublic --|> hr_employee_skill : one2many
HrEmployeePublic --|> hr_employee_skill : one2many
class "hr.employee" as hr_employee
hr_employee_skill --> hr_employee : many2one
HrJob --|> hr_job_skill : one2many
HrJob --|> hr_job_skill : one2many
HrJob .. hr_skill : many2many
class "hr.job" as hr_job
hr_job_skill --> hr_job : many2one
hr_resume_line --> hr_employee : many2one
hr_resume_line --> hr_resume_line_type : many2one
hr_skill --> hr_skill_type : many2one
hr_skill_level --> hr_skill_type : many2one
hr_skill_type --|> hr_skill : one2many
hr_skill_type --|> hr_skill_level : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
