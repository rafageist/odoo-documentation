<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# iot.device

- Module: [[docs/Enterprise Addons/iot/iot|iot]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/iot_device.py`
- Python classes: `IotDevice`
- Description: IOT Device

## Field footprint

- Detected fields: 15
- Field types: `Boolean` x 2, `Char` x 5, `Many2many` x 1, `Many2one` x 3, `Selection` x 4
- Relation fields: 4

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`, related `iot_id.company_id`)
- `connected_status`: `Selection`
- `connection`: `Selection`
- `display_url`: `Char` (comodel `Display URL`)
- `identifier`: `Char`
- `iot_id`: `Many2one` (comodel `iot.box`)
- `iot_ip`: `Char` (related `iot_id.ip`)
- `is_scanner`: `Boolean` (compute `_compute_is_scanner`)
- `keyboard_layout`: `Many2one` (comodel `iot.keyboard.layout`)
- `manual_measurement`: `Boolean` (comodel `Manual Measurement`, compute `_compute_manual_measurement`)
- `manufacturer`: `Char`
- `name`: `Char` (comodel `Name`)
- `report_ids`: `Many2many` (comodel `ir.actions.report`)
- `subtype`: `Selection`
- `type`: `Selection`

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_display_name`, `_compute_is_scanner`, `_compute_manual_measurement`
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
title iot.device - Direct Relations
class "iot.device" as iot_device
class "iot.box" as iot_box
class "iot.keyboard.layout" as iot_keyboard_layout
class "ir.actions.report" as ir_actions_report
class "res.company" as res_company
iot_device --> iot_box : iot_id
iot_device .. ir_actions_report : report_ids
iot_device --> res_company : company_id
iot_device --> iot_keyboard_layout : keyboard_layout
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/iot/Models]]

<!-- GENERATED:MODEL -->
