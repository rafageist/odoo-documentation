<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Barcode

- Version: v19
- Category: community
- Source: odoo19/addons/barcodes
- Dependencies: [[Odoo 19/Community Addons/web/web|web]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
