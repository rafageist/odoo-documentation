<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# export.one2many.multiple

- Module: [[docs/Community Addons/test_import_export/test_import_export|test_import_export]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/models_export_impex.py`
- Python classes: `ExportOne2manyMultiple`
- Description: Export One To Many Multiple

## Field footprint

- Detected fields: 4
- Field types: `Integer` x 1, `Many2one` x 1, `One2many` x 2
- Relation fields: 3

## Sample fields

- `child1`: `One2many` (comodel `export.one2many.child.1`)
- `child2`: `One2many` (comodel `export.one2many.child.2`)
- `const`: `Integer`
- `parent_id`: `Many2one` (comodel `export.one2many.recursive`)

## Method hints

- Detected methods: 0
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Direct relation diagram

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
title export.one2many.multiple - Direct Relations
class "export.one2many.multiple" as export_one2many_multiple
class "export.one2many.child.1" as export_one2many_child_1
class "export.one2many.child.2" as export_one2many_child_2
class "export.one2many.recursive" as export_one2many_recursive
export_one2many_multiple --> export_one2many_recursive : parent_id
export_one2many_multiple --|> export_one2many_child_1 : child1
export_one2many_multiple --|> export_one2many_child_2 : child2
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/test_import_export/Models]]

<!-- GENERATED:MODEL -->
