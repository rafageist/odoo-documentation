<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Time Off in Payslips

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_payroll_holidays
- Dependencies: [[Odoo 18/Enterprise Addons/hr_holidays_gantt/hr_holidays_gantt|hr_holidays_gantt]], [[Odoo 18/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 18/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
## XML Artifacts (detected)

- Views: 8
- Actions: 4
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrContract`
- `HrLeave`
- `HrPayslip`
- `MailActivity`
- `MailActivityType`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Time Off in Payslips - Models and Relations
class HrContract
class HrLeave
class HrPayslip
class MailActivity
class MailActivityType
class ResCompany
class "res.users" as res_users
ResCompany --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
