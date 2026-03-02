<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents - Fleet

- Scope: Enterprise Addons
- Source: enterprise/documents_fleet
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Community Addons/fleet/fleet|fleet]]

## Summary

Fleet from documents

## XML Artifacts (detected)

- Views: 2
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `fleet.vehicle`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Documents - Fleet - Models and Relations
class "fleet.vehicle" as fleet_vehicle
class ResCompany
class "documents.document" as documents_document
ResCompany --> documents_document : many2one
class "documents.tag" as documents_tag
ResCompany .. documents_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




