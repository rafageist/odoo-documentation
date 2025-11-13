<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Internet of Things

- Version: v19
- Category: enterprise
- Source: enterprise19/iot
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/iot_base/iot_base|iot_base]]

## Summary

Basic models and helpers to support Internet of Things.

## XML Artifacts (detected)

- Views: 15
- Actions: 5
- Menus: 6
- Rules (ir.rule): 2
- Access CSV entries: 8

## Detected Models

- `iot.box`
- `iot.device`
- `iot.keyboard.layout`
- `IrActionsReport`
- `IrConfigParameter`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Internet of Things - Models and Relations
class "iot.box" as iot_box
class "iot.device" as iot_device
class "iot.keyboard.layout" as iot_keyboard_layout
class IrActionsReport
class IrConfigParameter
iot_box --|> iot_device : one2many
class "res.company" as res_company
iot_box --> res_company : many2one
iot_device --> iot_box : many2one
class "ir.actions.report" as ir_actions_report
iot_device .. ir_actions_report : many2many
iot_device --> res_company : many2one
iot_device --> iot_keyboard_layout : many2one
IrActionsReport .. iot_device : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
