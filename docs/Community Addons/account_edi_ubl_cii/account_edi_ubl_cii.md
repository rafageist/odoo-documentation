<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Import/Export electronic invoices with UBL/CII

- Scope: Community Addons
- Source: odoo/addons/account_edi_ubl_cii
- Dependencies: [[docs/Community Addons/account/account|account]]

## Generated coverage

- Models: 15
- XML files with UI/data artifacts: 2
- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 0

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
title Import/Export electronic invoices with UBL/CII - Generated Coverage
component "Module Overview" as overview
component "Models\n15" as models
component "Views / XML\n2 views\n2 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/account_edi_ubl_cii/Models|Models]] (15)
- Views and XML: [[docs/Community Addons/account_edi_ubl_cii/Views|Views]] (2 files)

## Key models

- `account.edi.common`
- `account.edi.xml.cii`
- `account.edi.xml.ubl_20`
- `account.edi.xml.ubl_21`
- `account.edi.xml.ubl_a_nz`
- `account.edi.xml.ubl_bis3`
- `account.edi.xml.ubl_de`
- `account.edi.xml.ubl_efff`
- `account.edi.xml.ubl_nl`
- `account.edi.xml.ubl_sg`
- `account.move`
- `account.move.send`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






