<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Worksheet

- Version: v18
- Category: enterprise
- Source: enterprise18/worksheet
- Dependencies: [[Odoo 18/Enterprise Addons/web_studio/web_studio|web_studio]]

## Summary

Create customizable worksheet

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `IrModel`
- `worksheet.template`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Worksheet - Models and Relations
class IrModel
class "worksheet.template" as worksheet_template
class "ir.model" as ir_model
worksheet_template --> ir_model : many2one
class "ir.actions.act_window" as ir_actions_act_window
worksheet_template --> ir_actions_act_window : many2one
class "res.company" as res_company
worksheet_template --> res_company : many2one
class "ir.ui.view" as ir_ui_view
worksheet_template --> ir_ui_view : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
