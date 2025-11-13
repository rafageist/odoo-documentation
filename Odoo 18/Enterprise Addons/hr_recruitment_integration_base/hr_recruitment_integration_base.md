<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Recruitment Integration Base

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_recruitment_integration_base
- Dependencies: [[Odoo 18/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
## XML Artifacts (detected)

- Views: 9
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `Job`
- `hr.job.post`
- `hr.recruitment.platform`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Recruitment Integration Base - Models and Relations
class Job
class "hr.job.post" as hr_job_post
class "hr.recruitment.platform" as hr_recruitment_platform
Job --|> hr_job_post : one2many
class "res.currency" as res_currency
Job --> res_currency : many2one
class "resource.calendar" as resource_calendar
Job --> resource_calendar : many2one
class "hr.job" as hr_job
hr_job_post --> hr_job : many2one
class "res.users" as res_users
hr_job_post --> res_users : many2one
hr_job_post --> hr_recruitment_platform : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
