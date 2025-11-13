<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Recruitment

- Version: v18
- Category: community
- Source: odoo/addons/hr_recruitment
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/calendar/calendar|calendar]], [[Odoo 18/Community Addons/utm/utm|utm]], [[Odoo 18/Community Addons/attachment_indexation/attachment_indexation|attachment_indexation]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 18/Community Addons/digest/digest|digest]]

## Summary

Track your recruitment pipeline

## XML Artifacts (detected)

- Views: 46
- Actions: 34
- Menus: 27
- Rules (ir.rule): 10
- Access CSV entries: 29

## Detected Models

- `CalendarEvent`
- `Digest`
- `hr.applicant`
- `hr.applicant.category`
- `hr.applicant.refuse.reason`
- `hr.candidate`
- `HrDepartment`
- `HrEmployee`
- `hr.job`
- `hr.job.platform`
- `hr.recruitment.degree`
- `hr.recruitment.source`
- `hr.recruitment.stage`
- `IrUiMenu`
- `MailActivityPlan`
- `ResCompany`
- `ResUsers`
- `UtmCampaign`
- `UtmSource`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Recruitment - Models and Relations
class CalendarEvent
class Digest
class "hr.applicant" as hr_applicant
class "hr.applicant.category" as hr_applicant_category
class "hr.applicant.refuse.reason" as hr_applicant_refuse_reason
class "hr.candidate" as hr_candidate
class HrDepartment
class HrEmployee
class "hr.job" as hr_job
class "hr.job.platform" as hr_job_platform
class "hr.recruitment.degree" as hr_recruitment_degree
class "hr.recruitment.source" as hr_recruitment_source
class "hr.recruitment.stage" as hr_recruitment_stage
class IrUiMenu
class MailActivityPlan
class ResCompany
class ResUsers
class UtmCampaign
class UtmSource
CalendarEvent --> hr_applicant : many2one
CalendarEvent --> hr_candidate : many2one
hr_applicant --> hr_candidate : many2one
hr_applicant --> hr_recruitment_stage : many2one
hr_applicant --> hr_recruitment_stage : many2one
hr_applicant .. hr_applicant_category : many2many
class "res.company" as res_company
hr_applicant --> res_company : many2one
class "res.users" as res_users
hr_applicant --> res_users : many2one
hr_applicant --> hr_job : many2one
class "hr.department" as hr_department
hr_applicant --> hr_department : many2one
class "ir.attachment" as ir_attachment
hr_applicant --|> ir_attachment : one2many
hr_applicant --> hr_applicant_refuse_reason : many2one
class "calendar.event" as calendar_event
hr_applicant --|> calendar_event : one2many
hr_applicant .. res_users : many2many
class "mail.template" as mail_template
hr_applicant_refuse_reason --> mail_template : many2one
hr_candidate --> res_company : many2one
hr_candidate --|> hr_applicant : one2many
class "res.partner" as res_partner
hr_candidate --> res_partner : many2one
hr_candidate --> hr_recruitment_degree : many2one
hr_candidate .. hr_applicant_category : many2many
hr_candidate --> res_users : many2one
class "hr.employee" as hr_employee
hr_candidate --> hr_employee : many2one
hr_candidate --|> calendar_event : one2many
hr_candidate --|> ir_attachment : one2many
HrEmployee --|> hr_candidate : one2many
hr_job --> res_partner : many2one
hr_job --|> hr_applicant : one2many
hr_job --> hr_employee : many2one
hr_job --> res_users : many2one
hr_job --|> ir_attachment : one2many
hr_job .. res_users : many2many
hr_job .. res_users : many2many
hr_job .. res_users : many2many
class "res.partner.industry" as res_partner_industry
hr_job --> res_partner_industry : many2one
hr_recruitment_source --> hr_job : many2one
class "mail.alias" as mail_alias
hr_recruitment_source --> mail_alias : many2one
class "utm.medium" as utm_medium
hr_recruitment_source --> utm_medium : many2one
hr_recruitment_stage .. hr_job : many2many
hr_recruitment_stage --> mail_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
