<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Peppol

- Scope: Community Addons
- Source: odoo/addons/account_peppol
- Dependencies: [[docs/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]

## Summary

This module is used to send/receive documents with PEPPOL

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 5
- Views: 8
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3
- Controller units: 1
- Frontend asset files: 3

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
title Peppol - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n8 views\n5 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/account_peppol/Models|Models]] (13)
- Views and XML: [[docs/Community Addons/account_peppol/Views|Views]] (5 files)
- Controllers: [[docs/Community Addons/account_peppol/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/account_peppol/Frontend|Frontend]] (3 files)

## Key models

- `account.edi.xml.ubl_20`
- `account.journal`
- `account.move`
- `account.move.send`
- `account.move.send.batch.wizard`
- `account.move.send.wizard`
- `account_edi_proxy_client.user`
- `account_peppol.service`
- `peppol.config.wizard`
- `peppol.registration`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






