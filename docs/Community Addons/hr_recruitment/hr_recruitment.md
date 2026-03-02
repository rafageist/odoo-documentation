<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Recruitment

- Scope: Community Addons
- Source: odoo/addons/hr_recruitment
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/calendar/calendar|calendar]], [[docs/Community Addons/utm/utm|utm]], [[docs/Community Addons/attachment_indexation/attachment_indexation|attachment_indexation]], [[docs/Community Addons/web_tour/web_tour|web_tour]], [[docs/Community Addons/digest/digest|digest]]

## Summary

Track your recruitment pipeline

## XML Artifacts (detected)

- Views: 46
- Actions: 34
- Menus: 28
- Rules (ir.rule): 8
- Access CSV entries: 31

## Detected Models

- `CalendarEvent`
- `DigestDigest`
- `hr.applicant`
- `hr.applicant.category`
- `hr.applicant.refuse.reason`
- `HrDepartment`
- `HrEmployee`
- `hr.job`
- `hr.job.platform`
- `hr.recruitment.degree`
- `hr.recruitment.source`
- `hr.recruitment.stage`
- `hr.talent.pool`
- `IrAttachment`
- `IrUiMenu`
- `MailActivityPlan`
- `ResCompany`
- `ResPartner`
- `ResUsers`
- `UtmCampaign`
- `UtmSource`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Recruitment - Models and Relations
class CalendarEvent
class DigestDigest
class "hr.applicant" as hr_applicant
class "hr.applicant.category" as hr_applicant_category
class "hr.applicant.refuse.reason" as hr_applicant_refuse_reason
class HrDepartment
class HrEmployee
class "hr.job" as hr_job
class "hr.job.platform" as hr_job_platform
class "hr.recruitment.degree" as hr_recruitment_degree
class "hr.recruitment.source" as hr_recruitment_source
class "hr.recruitment.stage" as hr_recruitment_stage
class "hr.talent.pool" as hr_talent_pool
class IrAttachment
class IrUiMenu
class MailActivityPlan
class ResCompany
class ResPartner
class ResUsers
class UtmCampaign
class UtmSource
CalendarEvent --> hr_applicant : many2one
class "res.partner" as res_partner
hr_applicant --> res_partner : many2one
hr_applicant --> hr_recruitment_degree : many2one
class "hr.employee" as hr_employee
hr_applicant --> hr_employee : many2one
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
hr_applicant .. hr_talent_pool : many2many
hr_applicant --> hr_applicant : many2one
class "mail.template" as mail_template
hr_applicant_refuse_reason --> mail_template : many2one
HrEmployee --|> hr_applicant : one2many
hr_job --> res_partner : many2one
hr_job --|> hr_applicant : one2many
hr_job --> hr_employee : many2one
hr_job --|> ir_attachment : one2many
hr_job .. res_users : many2many
hr_job .. res_users : many2many
hr_job .. res_users : many2many
class "res.partner.industry" as res_partner_industry
hr_job --> res_partner_industry : many2one
hr_job --> hr_recruitment_degree : many2one
hr_job --|> hr_recruitment_source : one2many
hr_recruitment_source --> hr_job : many2one
class "mail.alias" as mail_alias
hr_recruitment_source --> mail_alias : many2one
class "utm.medium" as utm_medium
hr_recruitment_source --> utm_medium : many2one
class "utm.campaign" as utm_campaign
hr_recruitment_source --> utm_campaign : many2one
hr_recruitment_stage .. hr_job : many2many
hr_recruitment_stage --> mail_template : many2one
hr_talent_pool --> res_company : many2one
hr_talent_pool --> res_users : many2one
hr_talent_pool .. hr_applicant : many2many
hr_talent_pool .. hr_applicant_category : many2many
ResPartner --|> hr_applicant : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





