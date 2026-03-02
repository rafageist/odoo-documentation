<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Time Off in Payslips

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/hr_payroll_holidays
- Dependencies: [[Odoo 19/Enterprise Addons/hr_holidays_gantt/hr_holidays_gantt|hr_holidays_gantt]], [[Odoo 19/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

