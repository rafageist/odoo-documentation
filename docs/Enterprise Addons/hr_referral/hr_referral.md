<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Employee Referral

- Scope: Enterprise Addons
- Source: enterprise/hr_referral
- Dependencies: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]], [[docs/Community Addons/link_tracker/link_tracker|link_tracker]], [[docs/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]], [[docs/Enterprise Addons/hr_recruitment_reports/hr_recruitment_reports|hr_recruitment_reports]]

## Summary

Let your employees share job positions and refer their friends

## XML Artifacts (detected)

- Views: 43
- Actions: 22
- Menus: 14
- Rules (ir.rule): 11
- Access CSV entries: 23

## Detected Models

- `HrApplicant`
- `HrRecruitmentStage`
- `HrJob`
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
!include ../../../templates/DiagramStyles.puml
title Employee Referral - Models and Relations
class HrApplicant
class HrRecruitmentStage
class HrJob
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
HrApplicant --> res_users : many2one
HrApplicant --|> hr_referral_points : one2many
HrApplicant --> hr_referral_friend : many2one
class "hr.recruitment.stage" as hr_recruitment_stage
HrApplicant --> hr_recruitment_stage : many2one
class "utm.campaign" as utm_campaign
HrJob --> utm_campaign : many2one
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




