
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Worksheet for Quality Control

- Scope: Enterprise Addons
- Source: enterprise/quality_control_worksheet
- Dependencies: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]], [[docs/Enterprise Addons/worksheet/worksheet|worksheet]]

## Summary

Create custom worksheet for quality control

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 4
- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2
- Controller units: 0
- Frontend asset files: 4

## Module map

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title Worksheet for Quality Control - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n3 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n1 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/quality_control_worksheet/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/quality_control_worksheet/Views|Views]] (4 files)
- Frontend: [[docs/Enterprise Addons/quality_control_worksheet/Frontend|Frontend]] (4 files)

## Key models

- `quality.check`
- `quality.check.wizard`
- `quality.point`
- `report.quality_control.quality_worksheet`
- `worksheet.template`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



