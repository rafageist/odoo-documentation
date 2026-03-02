<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Appraisals

- Scope: Enterprise Addons
- Source: enterprise/hr_appraisal
- Dependencies: [[docs/Community Addons/calendar/calendar|calendar]], [[docs/Enterprise Addons/hr_gantt/hr_gantt|hr_gantt]]

## Summary

Assess your employees

## XML Artifacts (detected)

- Views: 37
- Actions: 18
- Menus: 12
- Rules (ir.rule): 14
- Access CSV entries: 15

## Detected Models

- `hr.appraisal`
- `hr.appraisal.goal`
- `hr.appraisal.goal.tag`
- `hr.appraisal.note`
- `hr.appraisal.template`
- `HrDepartment`
- `HrEmployee`
- `HrEmployeePublic`
- `MailTemplate`
- `ResCompany`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Appraisals - Models and Relations
class "hr.appraisal" as hr_appraisal
class "hr.appraisal.goal" as hr_appraisal_goal
class "hr.appraisal.goal.tag" as hr_appraisal_goal_tag
class "hr.appraisal.note" as hr_appraisal_note
class "hr.appraisal.template" as hr_appraisal_template
class HrDepartment
class HrEmployee
class HrEmployeePublic
class MailTemplate
class ResCompany
class ResUsers
class "hr.employee" as hr_employee
hr_appraisal --> hr_employee : many2one
class "res.users" as res_users
hr_appraisal --> res_users : many2one
class "res.company" as res_company
hr_appraisal --> res_company : many2one
class "hr.department" as hr_department
hr_appraisal --> hr_department : many2one
class "hr.job" as hr_job
hr_appraisal --> hr_job : many2one
hr_appraisal --> hr_appraisal : many2one
hr_appraisal --> hr_appraisal_template : many2one
hr_appraisal .. hr_employee : many2many
hr_appraisal .. hr_employee : many2many
hr_appraisal --> hr_appraisal_note : many2one
hr_appraisal --> hr_appraisal : many2one
hr_appraisal_goal .. hr_employee : many2many
hr_appraisal_goal .. hr_employee : many2many
hr_appraisal_goal --> res_company : many2one
hr_appraisal_goal .. hr_employee : many2many
hr_appraisal_goal .. hr_department : many2many
hr_appraisal_goal .. hr_job : many2many
hr_appraisal_goal .. hr_appraisal_goal_tag : many2many
hr_appraisal_goal --> hr_appraisal_goal : many2one
hr_appraisal_goal --> hr_appraisal_goal : many2one
hr_appraisal_goal --|> hr_appraisal_goal : one2many
hr_appraisal_note --> res_company : many2one
hr_appraisal_template --> res_company : many2one
hr_appraisal_template .. hr_department : many2many
HrDepartment .. hr_appraisal_template : many2many
class "res.partner" as res_partner
HrEmployee --> res_partner : many2one
HrEmployee --|> hr_appraisal : one2many
HrEmployee .. hr_appraisal_goal : many2many
HrEmployee --> hr_appraisal : many2one
HrEmployeePublic --> res_users : many2one
HrEmployeePublic --> hr_appraisal : many2one
ResCompany --|> hr_appraisal_note : one2many
class "mail.template" as mail_template
ResCompany --> mail_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



