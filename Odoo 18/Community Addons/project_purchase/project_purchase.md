<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Project Purchase

- Version: v18
- Category: community
- Source: odoo/addons/project_purchase
- Dependencies: [[Odoo 18/Community Addons/purchase/purchase|purchase]], [[Odoo 18/Community Addons/project_account/project_account|project_account]]

## Summary

Monitor purchase in project

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Project`
- `PurchaseOrder`
- `PurchaseOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project Purchase - Models and Relations
class Project
class PurchaseOrder
class PurchaseOrderLine
class "project.project" as project_project
PurchaseOrder --> project_project : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
