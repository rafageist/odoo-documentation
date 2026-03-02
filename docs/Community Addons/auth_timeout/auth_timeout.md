<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Auth Timeout

- Scope: Community Addons
- Source: odoo/addons/auth_timeout
- Dependencies: [[docs/Community Addons/auth_totp/auth_totp|auth_totp]], [[docs/Community Addons/auth_totp_mail/auth_totp_mail|auth_totp_mail]], [[docs/Community Addons/auth_passkey/auth_passkey|auth_passkey]], [[docs/Community Addons/bus/bus|bus]]

## Summary

Ask for authentication after user inactivity

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 3
- Frontend asset files: 2

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
title Auth Timeout - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n1 views\n1 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/auth_timeout/Models|Models]] (5)
- Views and XML: [[docs/Community Addons/auth_timeout/Views|Views]] (1 files)
- Controllers: [[docs/Community Addons/auth_timeout/Controllers|Controllers]] (3)
- Frontend: [[docs/Community Addons/auth_timeout/Frontend|Frontend]] (2 files)

## Key models

- `auth_totp.device`
- `ir.http`
- `ir.websocket`
- `res.groups`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






