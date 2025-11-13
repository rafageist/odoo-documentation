<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Time Off

- Version: v19
- Category: community
- Source: odoo19/addons/hr_holidays
- Dependencies: [[Odoo 19/Community Addons/hr/hr|hr]], [[Odoo 19/Community Addons/calendar/calendar|calendar]], [[Odoo 19/Community Addons/resource/resource|resource]]

## Summary

Allocate time off and follow leave requests

## XML Artifacts (detected)

- Views: 70
- Actions: 42
- Menus: 19
- Rules (ir.rule): 26
- Access CSV entries: 27

## Detected Models

- `CalendarEvent`
- `HrDepartment`
- `HrEmployee`
- `HrEmployeePublic`
- `hr.leave`
- `hr.leave.accrual.plan`
- `hr.leave.accrual.level`
- `hr.leave.allocation`
- `hr.leave.mandatory.day`
- `hr.leave.type`
- `HrVersion`
- `MailActivityType`
- `MailMessageSubtype`
- `ResourceCalendarLeaves`
- `ResourceCalendar`
- `ResourceResource`
- `ResPartner`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Time Off - Models and Relations
class CalendarEvent
class HrDepartment
class HrEmployee
class HrEmployeePublic
class "hr.leave" as hr_leave
class "hr.leave.accrual.plan" as hr_leave_accrual_plan
class "hr.leave.accrual.level" as hr_leave_accrual_level
class "hr.leave.allocation" as hr_leave_allocation
class "hr.leave.mandatory.day" as hr_leave_mandatory_day
class "hr.leave.type" as hr_leave_type
class HrVersion
class MailActivityType
class MailMessageSubtype
class ResourceCalendarLeaves
class ResourceCalendar
class ResourceResource
class ResPartner
class ResUsers
class "res.users" as res_users
HrEmployee --> res_users : many2one
HrEmployee --> hr_leave_type : many2one
HrEmployeePublic --> res_users : many2one
hr_leave --> res_users : many2one
hr_leave --> hr_leave_type : many2one
class "hr.employee" as hr_employee
hr_leave --> hr_employee : many2one
class "res.company" as res_company
hr_leave --> res_company : many2one
class "hr.department" as hr_department
hr_leave --> hr_department : many2one
class "resource.calendar" as resource_calendar
hr_leave --> resource_calendar : many2one
class "calendar.event" as calendar_event
hr_leave --> calendar_event : many2one
hr_leave --> hr_employee : many2one
hr_leave --> hr_employee : many2one
class "ir.attachment" as ir_attachment
hr_leave --|> ir_attachment : one2many
hr_leave .. ir_attachment : many2many
hr_leave_accrual_plan --> hr_leave_type : many2one
hr_leave_accrual_plan --|> hr_leave_accrual_level : one2many
hr_leave_accrual_plan --|> hr_leave_allocation : one2many
hr_leave_accrual_plan --> res_company : many2one
hr_leave_accrual_level --> hr_leave_accrual_plan : many2one
hr_leave_allocation --> hr_leave_type : many2one
hr_leave_allocation --> hr_employee : many2one
hr_leave_allocation --> hr_employee : many2one
hr_leave_allocation --> hr_employee : many2one
hr_leave_allocation --> hr_employee : many2one
hr_leave_allocation --> hr_department : many2one
hr_leave_allocation --> hr_leave_accrual_plan : many2one
hr_leave_mandatory_day --> res_company : many2one
hr_leave_mandatory_day --> resource_calendar : many2one
hr_leave_mandatory_day .. hr_department : many2many
class "hr.job" as hr_job
hr_leave_mandatory_day .. hr_job : many2many
hr_leave_type --> ir_attachment : many2one
hr_leave_type --> res_company : many2one
class "res.country" as res_country
hr_leave_type --> res_country : many2one
hr_leave_type .. res_users : many2many
class "mail.message.subtype" as mail_message_subtype
hr_leave_type --> mail_message_subtype : many2one
hr_leave_type --> mail_message_subtype : many2one
hr_leave_type --|> hr_leave_accrual_plan : one2many
ResourceCalendarLeaves --> hr_leave : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
