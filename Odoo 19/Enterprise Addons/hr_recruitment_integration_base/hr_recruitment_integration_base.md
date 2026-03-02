<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Recruitment Integration Base

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/hr_recruitment_integration_base
- Dependencies: [[Odoo 19/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]

## XML Artifacts (detected)

- Views: 10
- Actions: 3
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `HrApplicant`
- `HrJob`
- `hr.job.post`
- `hr.recruitment.platform`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Recruitment Integration Base - Models and Relations
class HrApplicant
class HrJob
class "hr.job.post" as hr_job_post
class "hr.recruitment.platform" as hr_recruitment_platform
HrJob --|> hr_job_post : one2many
class "res.currency" as res_currency
HrJob --> res_currency : many2one
class "resource.calendar" as resource_calendar
HrJob --> resource_calendar : many2one
class "hr.job" as hr_job
hr_job_post --> hr_job : many2one
class "res.users" as res_users
hr_job_post --> res_users : many2one
hr_job_post --> hr_recruitment_platform : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

