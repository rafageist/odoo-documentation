<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Skills Management

- Version: v18
- Category: community
- Source: odoo/addons/hr_skills
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]]

## Summary

Manage skills, knowledge and resume of your employees

## XML Artifacts (detected)

- Views: 26
- Actions: 9
- Menus: 4
- Rules (ir.rule): 9
- Access CSV entries: 17

## Detected Models

- `Employee`
- `EmployeePublic`
- `hr.employee.skill`
- `hr.employee.skill.log`
- `hr.resume.line`
- `hr.resume.line.type`
- `hr.skill`
- `hr.skill.level`
- `hr.skill.type`
- `Resource`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Skills Management - Models and Relations
class Employee
class EmployeePublic
class "hr.employee.skill" as hr_employee_skill
class "hr.employee.skill.log" as hr_employee_skill_log
class "hr.resume.line" as hr_resume_line
class "hr.resume.line.type" as hr_resume_line_type
class "hr.skill" as hr_skill
class "hr.skill.level" as hr_skill_level
class "hr.skill.type" as hr_skill_type
class Resource
class User
Employee --|> hr_resume_line : one2many
Employee --|> hr_employee_skill : one2many
Employee .. hr_skill : many2many
EmployeePublic --|> hr_resume_line : one2many
EmployeePublic --|> hr_employee_skill : one2many
class "hr.employee" as hr_employee
hr_employee_skill --> hr_employee : many2one
hr_employee_skill --> hr_skill : many2one
hr_employee_skill --> hr_skill_level : many2one
hr_employee_skill --> hr_skill_type : many2one
hr_employee_skill_log --> hr_employee : many2one
class "hr.department" as hr_department
hr_employee_skill_log --> hr_department : many2one
hr_employee_skill_log --> hr_skill : many2one
hr_employee_skill_log --> hr_skill_level : many2one
hr_employee_skill_log --> hr_skill_type : many2one
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
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
