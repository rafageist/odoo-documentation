<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Appraisals

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_appraisal
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/calendar/calendar|calendar]], [[Odoo 18/Enterprise Addons/web_gantt/web_gantt|web_gantt]]

## Summary

Assess your employees

## XML Artifacts (detected)

- Views: 34
- Actions: 15
- Menus: 10
- Rules (ir.rule): 13
- Access CSV entries: 13

## Detected Models

- `CalendarEvent`
- `hr.appraisal`
- `hr.appraisal.goal`
- `hr.appraisal.goal.tag`
- `hr.appraisal.note`
- `hr.appraisal.template`
- `hr_department`
- `HrEmployee`
- `HrEmployeePublic`
- `MailTemplate`
- `ResCompany`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Appraisals - Models and Relations
class CalendarEvent
class "hr.appraisal" as hr_appraisal
class "hr.appraisal.goal" as hr_appraisal_goal
class "hr.appraisal.goal.tag" as hr_appraisal_goal_tag
class "hr.appraisal.note" as hr_appraisal_note
class "hr.appraisal.template" as hr_appraisal_template
class hr_department
class HrEmployee
class HrEmployeePublic
class MailTemplate
class ResCompany
class User
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
hr_appraisal .. res_users : many2many
class "calendar.event" as calendar_event
hr_appraisal .. calendar_event : many2many
hr_appraisal .. hr_employee : many2many
hr_appraisal --> hr_appraisal_note : many2one
hr_appraisal --> hr_appraisal : many2one
hr_appraisal_goal --> hr_employee : many2one
hr_appraisal_goal .. hr_employee : many2many
hr_appraisal_goal --> hr_employee : many2one
hr_appraisal_goal --> res_users : many2one
hr_appraisal_goal .. hr_appraisal_goal_tag : many2many
hr_appraisal_note --> res_company : many2one
hr_appraisal_template --> res_company : many2one
hr_department --> hr_appraisal_template : many2one
class "res.partner" as res_partner
HrEmployee --> res_partner : many2one
HrEmployee --|> hr_appraisal : one2many
ResCompany --|> hr_appraisal_note : one2many
ResCompany --> hr_appraisal_template : many2one
class "mail.template" as mail_template
ResCompany --> mail_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
