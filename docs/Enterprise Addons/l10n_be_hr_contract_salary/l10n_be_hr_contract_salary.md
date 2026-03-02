<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Salary Configurator (Belgium)

- Scope: Enterprise Addons
- Source: enterprise/l10n_be_hr_contract_salary
- Dependencies: [[docs/Enterprise Addons/hr_contract_salary_payroll/hr_contract_salary_payroll|hr_contract_salary_payroll]], [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/l10n_be_hr_payroll_fleet|l10n_be_hr_payroll_fleet]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



