<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Belgium - Payroll - Fleet

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_be_hr_payroll_fleet
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]], [[Odoo 19/Community Addons/fleet/fleet|fleet]]
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
- `L10n_BeDmfa`
- `HrEmployee`
- `HrPayslip`
- `HrVersion`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Fleet - Models and Relations
class FleetVehicle
class FleetVehicleLogContract
class FleetVehicleModel
class L10n_BeDmfa
class HrEmployee
class HrPayslip
class HrVersion
class "fleet.vehicle" as fleet_vehicle
L10n_BeDmfa --|> fleet_vehicle : one2many
HrPayslip --> fleet_vehicle : many2one
HrVersion --> fleet_vehicle : many2one
HrVersion --> fleet_vehicle : many2one
class "fleet.vehicle.model" as fleet_vehicle_model
HrVersion --> fleet_vehicle_model : many2one
class "res.partner" as res_partner
HrVersion --> res_partner : many2one
HrVersion --> fleet_vehicle : many2one
HrVersion --> fleet_vehicle_model : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
