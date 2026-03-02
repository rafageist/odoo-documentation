<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Barcode - GS1 Nomenclature

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/barcodes_gs1_nomenclature
- Dependencies: [[Odoo 19/Community Addons/barcodes/barcodes|barcodes]], [[Odoo 19/Community Addons/uom/uom|uom]]

## Summary

Parse barcodes according to the GS1-128 specifications

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `BarcodeNomenclature`
- `BarcodeRule`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Barcode - GS1 Nomenclature - Models and Relations
class BarcodeNomenclature
class BarcodeRule
class "uom.uom" as uom_uom
BarcodeRule --> uom_uom : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


