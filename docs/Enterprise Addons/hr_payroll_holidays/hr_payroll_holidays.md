<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Time Off in Payslips

- Scope: Enterprise Addons
- Source: enterprise/hr_payroll_holidays
- Dependencies: [[docs/Enterprise Addons/hr_holidays_gantt/hr_holidays_gantt|hr_holidays_gantt]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## XML Artifacts (detected)

- Views: 4
- Actions: 4
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrEmployee`
- `HrLeave`
- `HrPayslip`
- `HrVersion`
- `MailActivity`
- `MailActivityType`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Time Off in Payslips - Models and Relations
class HrEmployee
class HrLeave
class HrPayslip
class HrVersion
class MailActivity
class MailActivityType
class ResCompany
class "hr.leave" as hr_leave
HrEmployee --|> hr_leave : one2many
class "res.users" as res_users
ResCompany --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



