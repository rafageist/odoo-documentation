<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Project Purchase

- Version: v19
- Category: community
- Source: odoo19/addons/project_purchase
- Dependencies: [[Odoo 19/Community Addons/purchase/purchase|purchase]], [[Odoo 19/Community Addons/project_account/project_account|project_account]]

## Summary

Monitor purchase in project

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProjectProject`
- `PurchaseOrder`
- `PurchaseOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project Purchase - Models and Relations
class ProjectProject
class PurchaseOrder
class PurchaseOrderLine
class "project.project" as project_project
PurchaseOrder --> project_project : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
