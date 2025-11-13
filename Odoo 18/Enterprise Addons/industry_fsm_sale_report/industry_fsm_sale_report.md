<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Field Service Reports - Sale

- Version: v18
- Category: enterprise
- Source: enterprise18/industry_fsm_sale_report
- Dependencies: [[Odoo 18/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]], [[Odoo 18/Enterprise Addons/industry_fsm_report/industry_fsm_report|industry_fsm_report]]

## Summary

Create Reports for Field service workers

## XML Artifacts (detected)

- Views: 2
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProductProduct`
- `ProductTemplate`
- `ProjectProject`
- `Task`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Field Service Reports - Sale - Models and Relations
class ProductProduct
class ProductTemplate
class ProjectProject
class Task
class SaleOrderLine
class "worksheet.template" as worksheet_template
ProductTemplate --> worksheet_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
