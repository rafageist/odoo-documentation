<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Employee Referral

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_referral
- Dependencies: [[Odoo 18/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]], [[Odoo 18/Community Addons/link_tracker/link_tracker|link_tracker]], [[Odoo 18/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]], [[Odoo 18/Enterprise Addons/hr_recruitment_reports/hr_recruitment_reports|hr_recruitment_reports]]

## Summary

Let your employees share job positions and refer their friends

## XML Artifacts (detected)

- Views: 37
- Actions: 20
- Menus: 12
- Rules (ir.rule): 11
- Access CSV entries: 22

## Detected Models

- `Applicant`
- `RecruitmentStage`
- `Job`
- `hr.referral.alert`
- `hr.referral.friend`
- `hr.referral.level`
- `hr.referral.onboarding`
- `hr.referral.points`
- `hr.referral.reward`
- `ResCompany`
- `ResUsers`
- `UtmCampaign`
- `UtmSource`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Employee Referral - Models and Relations
class Applicant
class RecruitmentStage
class Job
class "hr.referral.alert" as hr_referral_alert
class "hr.referral.friend" as hr_referral_friend
class "hr.referral.level" as hr_referral_level
class "hr.referral.onboarding" as hr_referral_onboarding
class "hr.referral.points" as hr_referral_points
class "hr.referral.reward" as hr_referral_reward
class ResCompany
class ResUsers
class UtmCampaign
class UtmSource
class "res.users" as res_users
Applicant --> res_users : many2one
Applicant --|> hr_referral_points : one2many
Applicant --> hr_referral_friend : many2one
class "hr.recruitment.stage" as hr_recruitment_stage
Applicant --> hr_recruitment_stage : many2one
class "utm.campaign" as utm_campaign
Job --> utm_campaign : many2one
class "res.company" as res_company
hr_referral_alert --> res_company : many2one
hr_referral_alert .. res_users : many2many
hr_referral_onboarding --> res_company : many2one
class "hr.applicant" as hr_applicant
hr_referral_points --> hr_applicant : many2one
hr_referral_points --> hr_referral_reward : many2one
hr_referral_points --> res_users : many2one
hr_referral_points --> hr_recruitment_stage : many2one
hr_referral_points --> res_company : many2one
hr_referral_reward --> res_users : many2one
hr_referral_reward --> res_company : many2one
ResUsers --> hr_referral_level : many2one
ResUsers --|> hr_referral_points : one2many
class "utm.source" as utm_source
ResUsers --> utm_source : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
