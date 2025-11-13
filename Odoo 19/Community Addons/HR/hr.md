<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Employees

- Version: v19
- Category: community
- Source: odoo19/addons/hr
- Dependencies: [[Odoo 19/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 19/Community Addons/digest/digest|digest]], [[Odoo 19/Community Addons/phone_validation/phone_validation|phone_validation]], [[Odoo 19/Community Addons/resource_mail/resource_mail|resource_mail]], [[Odoo 19/Community Addons/web/web|web]]

## Summary

Centralize employee information

## XML Artifacts (detected)

- Views: 56
- Actions: 41
- Menus: 18
- Rules (ir.rule): 13
- Access CSV entries: 26

## Detected Models

- `DiscussChannel`
- `hr.contract.type`
- `hr.department`
- `hr.departure.reason`
- `hr.employee`
- `hr.employee.category`
- `hr.employee.public`
- `hr.job`
- `hr.payroll.structure.type`
- `hr.version`
- `hr.work.location`
- `IrUiMenu`
- `MailActivityPlan`
- `MailActivityPlanTemplate`
- `MailAlias`
- `ResourceResource`
- `ResourceCalendar`
- `ResourceCalendarLeaves`
- `ResCompany`
- `ResPartner`
- `ResPartnerBank`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Employees - Models and Relations
class DiscussChannel
class "hr.contract.type" as hr_contract_type
class "hr.department" as hr_department
class "hr.departure.reason" as hr_departure_reason
class "hr.employee" as hr_employee
class "hr.employee.category" as hr_employee_category
class "hr.employee.public" as hr_employee_public
class "hr.job" as hr_job
class "hr.payroll.structure.type" as hr_payroll_structure_type
class "hr.version" as hr_version
class "hr.work.location" as hr_work_location
class IrUiMenu
class MailActivityPlan
class MailActivityPlanTemplate
class MailAlias
class ResourceResource
class ResourceCalendar
class ResourceCalendarLeaves
class ResCompany
class ResPartner
class ResPartnerBank
class ResUsers
DiscussChannel .. hr_department : many2many
class "res.country" as res_country
hr_contract_type --> res_country : many2one
class "res.company" as res_company
hr_department --> res_company : many2one
hr_department --> hr_department : many2one
hr_department --|> hr_department : one2many
hr_department --> hr_employee : many2one
hr_department --|> hr_employee : one2many
hr_department --|> hr_job : one2many
class "mail.activity.plan" as mail_activity_plan
hr_department --|> mail_activity_plan : one2many
hr_department --> hr_department : many2one
hr_departure_reason --> res_country : many2one
hr_employee --> hr_version : many2one
hr_employee --> hr_version : many2one
hr_employee --|> hr_version : one2many
class "resource.resource" as resource_resource
hr_employee --> resource_resource : many2one
class "res.users" as res_users
hr_employee --> res_users : many2one
hr_employee --> res_company : many2one
hr_employee --> res_country : many2one
class "res.partner" as res_partner
hr_employee --> res_partner : many2one
hr_employee --> res_country : many2one
class "res.partner.bank" as res_partner_bank
hr_employee .. res_partner_bank : many2many
hr_employee --> res_partner_bank : many2one
hr_employee --> hr_employee : many2one
hr_employee --|> hr_employee : one2many
hr_employee --> hr_employee : many2one
hr_employee .. hr_employee_category : many2many
class "res.currency" as res_currency
hr_employee --> res_currency : many2one
hr_employee_category .. hr_employee : many2many
hr_employee_public --> hr_department : many2one
hr_employee_public --> hr_job : many2one
hr_employee_public --> res_company : many2one
hr_employee_public --> res_partner : many2one
hr_employee_public --> res_partner : many2one
hr_employee_public --> hr_work_location : many2one
hr_employee_public --> res_users : many2one
hr_employee_public --> resource_resource : many2one
class "resource.calendar" as resource_calendar
hr_employee_public --> resource_calendar : many2one
hr_employee_public --> hr_employee : many2one
hr_employee_public --|> hr_employee_public : one2many
hr_employee_public --> hr_employee_public : many2one
hr_employee_public --> hr_employee_public : many2one
hr_job --|> hr_employee : one2many
hr_job --> res_users : many2one
hr_job .. res_users : many2many
hr_job --> hr_department : many2one
hr_job --> res_company : many2one
hr_job --> hr_contract_type : many2one
hr_payroll_structure_type --> resource_calendar : many2one
hr_payroll_structure_type --> res_country : many2one
hr_version --> res_company : many2one
hr_version --> hr_employee : many2one
hr_version --> res_users : many2one
hr_version --> res_country : many2one
class "res.country.state" as res_country_state
hr_version .. res_country_state : many2many
hr_version --> res_country_state : many2one
hr_version --> res_country : many2one
hr_version --> hr_department : many2one
hr_version --> hr_job : many2one
hr_version --> res_partner : many2one
hr_version --> hr_work_location : many2one
hr_version --> hr_departure_reason : many2one
hr_version --> resource_calendar : many2one
hr_version --> hr_version : many2one
hr_version --> hr_payroll_structure_type : many2one
hr_version --> res_country : many2one
hr_version --> hr_contract_type : many2one
hr_version --> res_users : many2one
hr_work_location --> res_company : many2one
hr_work_location --> res_partner : many2one
MailActivityPlan --> hr_department : many2one
ResourceResource --|> hr_employee : one2many
ResourceResource --> hr_department : many2one
ResPartner --|> hr_employee : one2many
ResPartnerBank .. hr_employee : many2many
ResUsers --|> hr_employee : one2many
ResUsers --> hr_employee : many2one
ResUsers .. res_partner_bank : many2many
ResUsers --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
<!-- GENERATED:CATEGORY -->
---
tags: [odoo, v19, community, index, category]
---

# HR

Modules: 30

- [[Odoo 19/Community Addons/fleet/fleet|fleet]]
- [[Odoo 19/Community Addons/gamification/gamification|gamification]]
- [[Odoo 19/Community Addons/hr/hr|hr]]
- [[Odoo 19/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- [[Odoo 19/Community Addons/hr_calendar/hr_calendar|hr_calendar]]
- [[Odoo 19/Community Addons/hr_expense/hr_expense|hr_expense]]
- [[Odoo 19/Community Addons/hr_fleet/hr_fleet|hr_fleet]]
- [[Odoo 19/Community Addons/hr_gamification/hr_gamification|hr_gamification]]
- [[Odoo 19/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- [[Odoo 19/Community Addons/hr_holidays_attendance/hr_holidays_attendance|hr_holidays_attendance]]
- [[Odoo 19/Community Addons/hr_homeworking/hr_homeworking|hr_homeworking]]
- [[Odoo 19/Community Addons/hr_homeworking_calendar/hr_homeworking_calendar|hr_homeworking_calendar]]
- [[Odoo 19/Community Addons/hr_hourly_cost/hr_hourly_cost|hr_hourly_cost]]
- [[Odoo 19/Community Addons/hr_livechat/hr_livechat|hr_livechat]]
- [[Odoo 19/Community Addons/hr_maintenance/hr_maintenance|hr_maintenance]]
- [[Odoo 19/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]
- [[Odoo 19/Community Addons/hr_presence/hr_presence|hr_presence]]
- [[Odoo 19/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- [[Odoo 19/Community Addons/hr_recruitment_skills/hr_recruitment_skills|hr_recruitment_skills]]
- [[Odoo 19/Community Addons/hr_recruitment_sms/hr_recruitment_sms|hr_recruitment_sms]]
- [[Odoo 19/Community Addons/hr_recruitment_survey/hr_recruitment_survey|hr_recruitment_survey]]
- [[Odoo 19/Community Addons/hr_skills/hr_skills|hr_skills]]
- [[Odoo 19/Community Addons/hr_skills_event/hr_skills_event|hr_skills_event]]
- [[Odoo 19/Community Addons/hr_skills_slides/hr_skills_slides|hr_skills_slides]]
- [[Odoo 19/Community Addons/hr_skills_survey/hr_skills_survey|hr_skills_survey]]
- [[Odoo 19/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- [[Odoo 19/Community Addons/hr_timesheet_attendance/hr_timesheet_attendance|hr_timesheet_attendance]]
- [[Odoo 19/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]]
- [[Odoo 19/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]]
- [[Odoo 19/Community Addons/lunch/lunch|lunch]]
<!-- GENERATED:CATEGORY -->
