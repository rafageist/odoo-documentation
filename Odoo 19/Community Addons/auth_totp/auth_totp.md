<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Two-Factor Authentication (TOTP)

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/auth_totp
- Dependencies: [[Odoo 19/Community Addons/web/web|web]]

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
!include ../../../Templates/DiagramStyles.puml
title Two-Factor Authentication (TOTP) - Models and Relations
class "auth_totp.device" as auth_totp_device
class ResUsers
ResUsers --|> auth_totp_device : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


