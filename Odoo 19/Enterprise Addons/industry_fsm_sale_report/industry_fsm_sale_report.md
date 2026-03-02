<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Field Service Reports - Sale

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/industry_fsm_sale_report
- Dependencies: [[Odoo 19/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]], [[Odoo 19/Enterprise Addons/industry_fsm_report/industry_fsm_report|industry_fsm_report]]

## Summary

Create Reports for Field service technicians

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
- `ProjectTask`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Field Service Reports - Sale - Models and Relations
class ProductProduct
class ProductTemplate
class ProjectProject
class ProjectTask
class SaleOrderLine
class "worksheet.template" as worksheet_template
ProductTemplate --> worksheet_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


