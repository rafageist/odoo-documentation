<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Payroll - Fleet

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_hr_payroll_fleet
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]], [[Odoo 18/Community Addons/fleet/fleet|fleet]]
## XML Artifacts (detected)

- Views: 10
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `FleetVehicle`
- `FleetVehicleLogContract`
- `FleetVehicleModel`
- `HrContract`
- `HrDMFAReport`
- `HrPayslip`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Fleet - Models and Relations
class FleetVehicle
class FleetVehicleLogContract
class FleetVehicleModel
class HrContract
class HrDMFAReport
class HrPayslip
class "fleet.vehicle" as fleet_vehicle
HrContract --> fleet_vehicle : many2one
HrContract --> fleet_vehicle : many2one
class "fleet.vehicle.model" as fleet_vehicle_model
HrContract --> fleet_vehicle_model : many2one
class "res.partner" as res_partner
HrContract --> res_partner : many2one
HrContract --> fleet_vehicle : many2one
HrContract --> fleet_vehicle_model : many2one
HrDMFAReport --|> fleet_vehicle : one2many
HrPayslip --> fleet_vehicle : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
