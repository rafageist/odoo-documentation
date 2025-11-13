<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Internet of Things

- Version: v18
- Category: enterprise
- Source: enterprise18/iot
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/web/web|web]]

## Summary

Basic models and helpers to support Internet of Things.

## XML Artifacts (detected)

- Views: 11
- Actions: 5
- Menus: 6
- Rules (ir.rule): 2
- Access CSV entries: 7

## Detected Models

- `iot.box`
- `iot.device`
- `iot.keyboard.layout`
- `IrActionReport`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Internet of Things - Models and Relations
class "iot.box" as iot_box
class "iot.device" as iot_device
class "iot.keyboard.layout" as iot_keyboard_layout
class IrActionReport
iot_box --|> iot_device : one2many
class "res.company" as res_company
iot_box --> res_company : many2one
iot_device --> iot_box : many2one
class "ir.actions.report" as ir_actions_report
iot_device .. ir_actions_report : many2many
iot_device --> res_company : many2one
iot_device --> iot_keyboard_layout : many2one
IrActionReport .. iot_device : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
