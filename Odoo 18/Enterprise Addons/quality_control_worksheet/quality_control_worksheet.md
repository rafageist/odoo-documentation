<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Worksheet for Quality Control

- Version: v18
- Category: enterprise
- Source: enterprise18/quality_control_worksheet
- Dependencies: [[Odoo 18/Enterprise Addons/quality_control/quality_control|quality_control]], [[Odoo 18/Enterprise Addons/worksheet/worksheet|worksheet]]

## Summary

Create custom worksheet for quality control

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `QualityPoint`
- `QualityCheck`
- `WorksheetTemplate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Worksheet for Quality Control - Models and Relations
class QualityPoint
class QualityCheck
class WorksheetTemplate
class "worksheet.template" as worksheet_template
QualityPoint --> worksheet_template : many2one
QualityCheck --> worksheet_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
