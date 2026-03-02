<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Fleet

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/fleet
- Dependencies: base (not documented), [[Odoo 19/Community Addons/mail/mail|mail]]

## Summary

Manage your fleet and track car costs

## XML Artifacts (detected)

- Views: 51
- Actions: 15
- Menus: 21
- Rules (ir.rule): 9
- Access CSV entries: 24

## Detected Models

- `fleet.service.type`
- `fleet.vehicle`
- `fleet.vehicle.assignation.log`
- `fleet.vehicle.log.contract`
- `fleet.vehicle.log.services`
- `fleet.vehicle.model`
- `fleet.vehicle.model.brand`
- `fleet.vehicle.model.category`
- `fleet.vehicle.odometer`
- `fleet.vehicle.state`
- `fleet.vehicle.tag`
- `MailActivityType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Fleet - Models and Relations
class "fleet.service.type" as fleet_service_type
class "fleet.vehicle" as fleet_vehicle
class "fleet.vehicle.assignation.log" as fleet_vehicle_assignation_log
class "fleet.vehicle.log.contract" as fleet_vehicle_log_contract
class "fleet.vehicle.log.services" as fleet_vehicle_log_services
class "fleet.vehicle.model" as fleet_vehicle_model
class "fleet.vehicle.model.brand" as fleet_vehicle_model_brand
class "fleet.vehicle.model.category" as fleet_vehicle_model_category
class "fleet.vehicle.odometer" as fleet_vehicle_odometer
class "fleet.vehicle.state" as fleet_vehicle_state
class "fleet.vehicle.tag" as fleet_vehicle_tag
class MailActivityType
class "res.users" as res_users
fleet_vehicle --> res_users : many2one
class "res.company" as res_company
fleet_vehicle --> res_company : many2one
class "res.currency" as res_currency
fleet_vehicle --> res_currency : many2one
class "res.country" as res_country
fleet_vehicle --> res_country : many2one
class "res.partner" as res_partner
fleet_vehicle --> res_partner : many2one
fleet_vehicle --> res_partner : many2one
fleet_vehicle --> fleet_vehicle_model : many2one
fleet_vehicle --> fleet_vehicle_model_brand : many2one
fleet_vehicle --|> fleet_vehicle_assignation_log : one2many
fleet_vehicle --|> fleet_vehicle_log_services : one2many
fleet_vehicle --|> fleet_vehicle_log_contract : one2many
fleet_vehicle --> fleet_vehicle_state : many2one
fleet_vehicle .. fleet_vehicle_tag : many2many
fleet_vehicle --> fleet_vehicle_model_category : many2one
fleet_vehicle_assignation_log --> fleet_vehicle : many2one
fleet_vehicle_assignation_log --> res_partner : many2one
fleet_vehicle_log_contract --> fleet_vehicle : many2one
fleet_vehicle_log_contract --> fleet_service_type : many2one
fleet_vehicle_log_contract --> res_company : many2one
fleet_vehicle_log_contract --> res_currency : many2one
fleet_vehicle_log_contract --> res_users : many2one
fleet_vehicle_log_contract --> res_partner : many2one
fleet_vehicle_log_contract .. fleet_service_type : many2many
fleet_vehicle_log_services --> fleet_vehicle : many2one
fleet_vehicle_log_services --> fleet_vehicle_model : many2one
fleet_vehicle_log_services --> fleet_vehicle_model_brand : many2one
fleet_vehicle_log_services --> res_users : many2one
fleet_vehicle_log_services --> fleet_vehicle_odometer : many2one
fleet_vehicle_log_services --> res_company : many2one
fleet_vehicle_log_services --> res_currency : many2one
fleet_vehicle_log_services --> res_partner : many2one
fleet_vehicle_log_services --> res_partner : many2one
fleet_vehicle_log_services --> fleet_service_type : many2one
fleet_vehicle_model --> fleet_vehicle_model_brand : many2one
fleet_vehicle_model --> fleet_vehicle_model_category : many2one
fleet_vehicle_model .. res_partner : many2many
fleet_vehicle_model_brand --|> fleet_vehicle_model : one2many
fleet_vehicle_odometer --> fleet_vehicle : many2one
fleet_vehicle_odometer --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


