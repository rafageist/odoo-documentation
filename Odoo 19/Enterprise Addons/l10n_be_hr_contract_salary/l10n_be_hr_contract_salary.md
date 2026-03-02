<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Salary Configurator (Belgium)

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_be_hr_contract_salary
- Dependencies: [[Odoo 19/Enterprise Addons/hr_contract_salary_payroll/hr_contract_salary_payroll|hr_contract_salary_payroll]], [[Odoo 19/Enterprise Addons/l10n_be_hr_payroll_fleet/l10n_be_hr_payroll_fleet|l10n_be_hr_payroll_fleet]]

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
- `HrContractSalaryOffer`
- `HrContractSalaryResume`
- `HrEmployee`
- `HrJob`
- `HrPayslip`
- `HrVersion`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Salary Configurator (Belgium) - Models and Relations
class FleetVehicleState
class HrContractSalaryOffer
class HrContractSalaryResume
class HrEmployee
class HrJob
class HrPayslip
class HrVersion
class "hr.contract.type" as hr_contract_type
HrContractSalaryOffer --> hr_contract_type : many2one
class "fleet.vehicle" as fleet_vehicle
HrContractSalaryOffer --> fleet_vehicle : many2one
HrContractSalaryOffer .. fleet_vehicle : many2many
HrVersion --> hr_contract_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

