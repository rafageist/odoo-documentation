<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Barcode

- Scope: Community Addons
- Source: odoo/addons/barcodes
- Dependencies: [[docs/Community Addons/web/web|web]]

## Summary

Scan and Parse Barcodes

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `barcode.nomenclature`
- `barcode.rule`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Barcode - Models and Relations
class "barcode.nomenclature" as barcode_nomenclature
class "barcode.rule" as barcode_rule
class ResCompany
barcode_nomenclature --|> barcode_rule : one2many
barcode_rule --> barcode_nomenclature : many2one
ResCompany --> barcode_nomenclature : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





