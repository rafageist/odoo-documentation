<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# fleet.vehicle.log.contract

- Module: [[docs/Community Addons/fleet/fleet|fleet]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/fleet_vehicle_log_contract.py`
- Python classes: `FleetVehicleLogContract`
- Description: Vehicle Contract
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 22
- Field types: `Boolean` x 3, `Char` x 2, `Date` x 3, `Html` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 7, `Monetary` x 2, `Selection` x 2
- Relation fields: 8

## Sample fields

- `active`: `Boolean`
- `amount`: `Monetary` (comodel `Cost`)
- `company_id`: `Many2one` (comodel `res.company`)
- `cost_frequency`: `Selection`
- `cost_generated`: `Monetary` (comodel `Recurring Cost`)
- `cost_subtype_id`: `Many2one` (comodel `fleet.service.type`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `company_id.currency_id`)
- `date`: `Date`
- `days_left`: `Integer` (compute `_compute_days_left`)
- `expiration_date`: `Date` (comodel `Contract Expiration Date`)
- `expires_today`: `Boolean` (compute `_compute_days_left`)
- `has_open_contract`: `Boolean` (compute `_compute_has_open_contract`)
- `ins_ref`: `Char` (comodel `Reference`)
- `insurer_id`: `Many2one` (comodel `res.partner`)
- `name`: `Char` (compute `_compute_contract_name`, store `True`)
- `notes`: `Html` (comodel `Terms and Conditions`)
- `purchaser_id`: `Many2one` (related `vehicle_id.driver_id`)
- `service_ids`: `Many2many` (comodel `fleet.service.type`)
- `start_date`: `Date` (comodel `Contract Start Date`)
- `state`: `Selection`

## Method hints

- Detected methods: 11
- Action methods: `action_close`, `action_draft`, `action_expire`, `action_open`
- Compute methods: `_compute_contract_name`, `_compute_days_left`, `_compute_has_open_contract`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title fleet.vehicle.log.contract - Direct Relations
class "fleet.vehicle.log.contract" as fleet_vehicle_log_contract
class "fleet.service.type" as fleet_service_type
class "fleet.vehicle" as fleet_vehicle
class "res.company" as res_company
class "res.currency" as res_currency
class "res.partner" as res_partner
class "res.users" as res_users
fleet_vehicle_log_contract --> fleet_vehicle : vehicle_id
fleet_vehicle_log_contract --> fleet_service_type : cost_subtype_id
fleet_vehicle_log_contract --> res_company : company_id
fleet_vehicle_log_contract --> res_currency : currency_id
fleet_vehicle_log_contract --> res_users : user_id
fleet_vehicle_log_contract --> res_partner : insurer_id
fleet_vehicle_log_contract .. fleet_service_type : service_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/fleet/Models]]

<!-- GENERATED:MODEL -->
