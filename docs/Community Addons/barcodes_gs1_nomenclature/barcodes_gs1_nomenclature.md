<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Barcode - GS1 Nomenclature

- Scope: Community Addons
- Source: odoo/addons/barcodes_gs1_nomenclature
- Dependencies: [[docs/Community Addons/barcodes/barcodes|barcodes]], [[docs/Community Addons/uom/uom|uom]]

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
!include ../../../templates/DiagramStyles.puml
title Barcode - GS1 Nomenclature - Models and Relations
class BarcodeNomenclature
class BarcodeRule
class "uom.uom" as uom_uom
BarcodeRule --> uom_uom : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





