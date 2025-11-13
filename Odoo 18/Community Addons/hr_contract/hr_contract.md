<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Employee Contracts

- Version: v18
- Category: community
- Source: odoo/addons/hr_contract
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]]
## XML Artifacts (detected)

- Views: 22
- Actions: 4
- Menus: 4
- Rules (ir.rule): 5
- Access CSV entries: 7

## Detected Models

- `hr.contract`
- `EmployeePublic`
- `Employee`
- `hr.payroll.structure.type`
- `IrUiMenu`
- `ResourceCalendar`
- `ResourceCalendarLeaves`
- `ResourceResource`
- `ResCompany`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Employee Contracts - Models and Relations
class "hr.contract" as hr_contract
class EmployeePublic
class Employee
class "hr.payroll.structure.type" as hr_payroll_structure_type
class IrUiMenu
class ResourceCalendar
class ResourceCalendarLeaves
class ResourceResource
class ResCompany
class User
hr_contract --> hr_payroll_structure_type : many2one
class "hr.employee" as hr_employee
hr_contract --> hr_employee : many2one
class "hr.department" as hr_department
hr_contract --> hr_department : many2one
class "hr.job" as hr_job
hr_contract --> hr_job : many2one
class "resource.calendar" as resource_calendar
hr_contract --> resource_calendar : many2one
class "res.company" as res_company
hr_contract --> res_company : many2one
class "res.country" as res_country
hr_contract --> res_country : many2one
class "hr.contract.type" as hr_contract_type
hr_contract --> hr_contract_type : many2one
class "res.users" as res_users
hr_contract --> res_users : many2one
Employee --|> hr_contract : one2many
Employee --> hr_contract : many2one
hr_payroll_structure_type --> resource_calendar : many2one
hr_payroll_structure_type --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
