<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Field Service Reports - Sale

- Scope: Enterprise Addons
- Source: enterprise/industry_fsm_sale_report
- Dependencies: [[docs/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]], [[docs/Enterprise Addons/industry_fsm_report/industry_fsm_report|industry_fsm_report]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




