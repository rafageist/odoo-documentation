<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Salary Configurator - Holidays

- Version: v19
- Category: enterprise
- Source: enterprise19/hr_contract_salary_holidays
- Dependencies: [[Odoo 19/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]], [[Odoo 19/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Automatically creates extra time-off on contract signature

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrVersion`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Salary Configurator - Holidays - Models and Relations
class HrVersion
class ResCompany
class "hr.leave.allocation" as hr_leave_allocation
HrVersion --> hr_leave_allocation : many2one
class "hr.leave.type" as hr_leave_type
ResCompany --> hr_leave_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
