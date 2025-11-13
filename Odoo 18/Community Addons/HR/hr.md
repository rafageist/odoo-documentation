<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Employees

- Version: v18
- Category: community
- Source: odoo/addons/hr
- Dependencies: [[Odoo 18/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 18/Community Addons/digest/digest|digest]], [[Odoo 18/Community Addons/phone_validation/phone_validation|phone_validation]], [[Odoo 18/Community Addons/resource_mail/resource_mail|resource_mail]], [[Odoo 18/Community Addons/web/web|web]]

## Summary

Centralize employee information

## XML Artifacts (detected)

- Views: 44
- Actions: 33
- Menus: 19
- Rules (ir.rule): 9
- Access CSV entries: 16

## Detected Models

- `Channel`
- `hr.contract.type`
- `hr.department`
- `hr.departure.reason`
- `hr.employee`
- `hr.employee.category`
- `hr.employee.public`
- `hr.job`
- `hr.work.location`
- `IrUiMenu`
- `MailActivityPlan`
- `MailActivityPLanTemplate`
- `Alias`
- `ResourceResource`
- `ResourceCalendar`
- `Company`
- `Partner`
- `ResPartnerBank`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Employees - Models and Relations
class Channel
class "hr.contract.type" as hr_contract_type
class "hr.department" as hr_department
class "hr.departure.reason" as hr_departure_reason
class "hr.employee" as hr_employee
class "hr.employee.category" as hr_employee_category
class "hr.employee.public" as hr_employee_public
class "hr.job" as hr_job
class "hr.work.location" as hr_work_location
class IrUiMenu
class MailActivityPlan
class MailActivityPLanTemplate
class Alias
class ResourceResource
class ResourceCalendar
class Company
class Partner
class ResPartnerBank
class User
Channel .. hr_department : many2many
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
class "res.users" as res_users
hr_employee --> res_users : many2one
hr_employee --> res_company : many2one
hr_employee --> res_country : many2one
class "res.country.state" as res_country_state
hr_employee --> res_country_state : many2one
hr_employee --> res_country : many2one
hr_employee --> res_country : many2one
hr_employee --> res_country : many2one
class "res.partner.bank" as res_partner_bank
hr_employee --> res_partner_bank : many2one
hr_employee --|> hr_employee : one2many
hr_employee .. hr_employee_category : many2many
hr_employee --> hr_departure_reason : many2one
class "res.currency" as res_currency
hr_employee --> res_currency : many2one
hr_employee_category .. hr_employee : many2many
hr_employee_public --> hr_employee : many2one
hr_employee_public --|> hr_employee_public : one2many
hr_employee_public --> hr_employee_public : many2one
hr_employee_public --> hr_employee_public : many2one
hr_job --|> hr_employee : one2many
hr_job --> hr_department : many2one
hr_job --> res_company : many2one
hr_job --> hr_contract_type : many2one
hr_work_location --> res_company : many2one
class "res.partner" as res_partner
hr_work_location --> res_partner : many2one
MailActivityPlan --> hr_department : many2one
ResourceResource --|> hr_employee : one2many
Partner --|> hr_employee : one2many
User --|> hr_employee : one2many
User --> hr_employee : many2one
User --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
<!-- GENERATED:CATEGORY -->
---
tags: [odoo, v18, community, index, category]
---

# HR

Modules: 33

- [[Odoo 18/Community Addons/fleet/fleet|fleet]]
- [[Odoo 18/Community Addons/gamification/gamification|gamification]]
- [[Odoo 18/Community Addons/hr/hr|hr]]
- [[Odoo 18/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- [[Odoo 18/Community Addons/hr_calendar/hr_calendar|hr_calendar]]
- [[Odoo 18/Community Addons/hr_contract/hr_contract|hr_contract]]
- [[Odoo 18/Community Addons/hr_expense/hr_expense|hr_expense]]
- [[Odoo 18/Community Addons/hr_fleet/hr_fleet|hr_fleet]]
- [[Odoo 18/Community Addons/hr_gamification/hr_gamification|hr_gamification]]
- [[Odoo 18/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- [[Odoo 18/Community Addons/hr_holidays_attendance/hr_holidays_attendance|hr_holidays_attendance]]
- [[Odoo 18/Community Addons/hr_holidays_contract/hr_holidays_contract|hr_holidays_contract]]
- [[Odoo 18/Community Addons/hr_homeworking/hr_homeworking|hr_homeworking]]
- [[Odoo 18/Community Addons/hr_homeworking_calendar/hr_homeworking_calendar|hr_homeworking_calendar]]
- [[Odoo 18/Community Addons/hr_hourly_cost/hr_hourly_cost|hr_hourly_cost]]
- [[Odoo 18/Community Addons/hr_livechat/hr_livechat|hr_livechat]]
- [[Odoo 18/Community Addons/hr_maintenance/hr_maintenance|hr_maintenance]]
- [[Odoo 18/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]
- [[Odoo 18/Community Addons/hr_presence/hr_presence|hr_presence]]
- [[Odoo 18/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- [[Odoo 18/Community Addons/hr_recruitment_skills/hr_recruitment_skills|hr_recruitment_skills]]
- [[Odoo 18/Community Addons/hr_recruitment_sms/hr_recruitment_sms|hr_recruitment_sms]]
- [[Odoo 18/Community Addons/hr_recruitment_survey/hr_recruitment_survey|hr_recruitment_survey]]
- [[Odoo 18/Community Addons/hr_skills/hr_skills|hr_skills]]
- [[Odoo 18/Community Addons/hr_skills_slides/hr_skills_slides|hr_skills_slides]]
- [[Odoo 18/Community Addons/hr_skills_survey/hr_skills_survey|hr_skills_survey]]
- [[Odoo 18/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- [[Odoo 18/Community Addons/hr_timesheet_attendance/hr_timesheet_attendance|hr_timesheet_attendance]]
- [[Odoo 18/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]]
- [[Odoo 18/Community Addons/hr_work_entry_contract/hr_work_entry_contract|hr_work_entry_contract]]
- [[Odoo 18/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]]
- [[Odoo 18/Community Addons/lunch/lunch|lunch]]
- [[Odoo 18/Community Addons/test_hr_contract_calendar/test_hr_contract_calendar|test_hr_contract_calendar]]
<!-- GENERATED:CATEGORY -->
