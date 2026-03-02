
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Salary Configurator - Holidays

- Scope: Enterprise Addons
- Source: enterprise/hr_contract_salary_holidays
- Dependencies: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]], [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

