<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Salary Configurator (Belgium)

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_hr_contract_salary
- Dependencies: [[Odoo 18/Enterprise Addons/hr_contract_salary_payroll/hr_contract_salary_payroll|hr_contract_salary_payroll]], [[Odoo 18/Enterprise Addons/l10n_be_hr_payroll_fleet/l10n_be_hr_payroll_fleet|l10n_be_hr_payroll_fleet]]

## Summary

Salary Package Configurator

## XML Artifacts (detected)

- Views: 11
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `FleetVehicleState`
- `HrContract`
- `HrContractSalaryOffer`
- `HrContractSalaryResume`
- `HrEmployee`
- `HrJob`
- `HrPayslip`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Salary Configurator (Belgium) - Models and Relations
class FleetVehicleState
class HrContract
class HrContractSalaryOffer
class HrContractSalaryResume
class HrEmployee
class HrJob
class HrPayslip
class "hr.contract.type" as hr_contract_type
HrContract --> hr_contract_type : many2one
HrContractSalaryOffer --> hr_contract_type : many2one
class "fleet.vehicle" as fleet_vehicle
HrContractSalaryOffer --> fleet_vehicle : many2one
HrContractSalaryOffer .. fleet_vehicle : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
