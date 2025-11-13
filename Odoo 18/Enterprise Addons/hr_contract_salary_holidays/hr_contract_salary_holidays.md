<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Salary Configurator - Holidays

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_contract_salary_holidays
- Dependencies: [[Odoo 18/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]], [[Odoo 18/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Automatically creates extra time-off on contract signature

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrContract`
- `Company`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Salary Configurator - Holidays - Models and Relations
class HrContract
class Company
class "hr.leave.allocation" as hr_leave_allocation
HrContract --> hr_leave_allocation : many2one
class "hr.leave.type" as hr_leave_type
Company --> hr_leave_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
