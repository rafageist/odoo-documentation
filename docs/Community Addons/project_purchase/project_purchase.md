<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Project Purchase

- Scope: Community Addons
- Source: odoo/addons/project_purchase
- Dependencies: [[docs/Community Addons/purchase/purchase|purchase]], [[docs/Community Addons/project_account/project_account|project_account]]

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
!include ../../../templates/DiagramStyles.puml
title Project Purchase - Models and Relations
class ProjectProject
class PurchaseOrder
class PurchaseOrderLine
class "project.project" as project_project
PurchaseOrder --> project_project : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





