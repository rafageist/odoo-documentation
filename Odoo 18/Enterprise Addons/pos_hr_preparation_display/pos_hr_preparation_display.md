<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# PoS Preparation Display HR

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_hr_preparation_display
- Dependencies: [[Odoo 18/Enterprise Addons/pos_preparation_display/pos_preparation_display|pos_preparation_display]], [[Odoo 18/Community Addons/pos_hr/pos_hr|pos_hr]]

## Summary

Display Orders for Preparation stage.

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosPreparationDisplayOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title PoS Preparation Display HR - Models and Relations
class PosPreparationDisplayOrder
class "hr.employee" as hr_employee
PosPreparationDisplayOrder --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
