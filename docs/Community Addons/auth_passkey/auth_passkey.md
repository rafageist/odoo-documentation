<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Passkeys

- Scope: Community Addons
- Source: odoo/addons/auth_passkey
- Dependencies: [[docs/Community Addons/base_setup/base_setup|base_setup]], [[docs/Community Addons/web/web|web]]

## Summary

Log in with a Passkey

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 4
- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 3
- Access CSV entries: 5
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
title Passkeys - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n6 views\n4 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n3 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/auth_passkey/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/auth_passkey/Views|Views]] (4 files)
- Controllers: [[docs/Community Addons/auth_passkey/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/auth_passkey/Frontend|Frontend]] (3 files)

## Key models

- `auth.passkey.key`
- `auth.passkey.key.create`
- `res.users`
- `res.users.identitycheck`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






