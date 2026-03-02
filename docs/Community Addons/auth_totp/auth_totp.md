<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Two-Factor Authentication (TOTP)

- Scope: Community Addons
- Source: odoo/addons/auth_totp
- Dependencies: [[docs/Community Addons/web/web|web]]

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 4
- Access CSV entries: 3

## Detected Models

- `auth_totp.device`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Two-Factor Authentication (TOTP) - Models and Relations
class "auth_totp.device" as auth_totp_device
class ResUsers
ResUsers --|> auth_totp_device : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





