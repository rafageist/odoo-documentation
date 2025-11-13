<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Two-Factor Authentication (TOTP)

- Version: v18
- Category: community
- Source: odoo/addons/auth_totp
- Dependencies: [[Odoo 18/Community Addons/web/web|web]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 4
- Access CSV entries: 2

## Detected Models

- `auth_totp.device`
- `Users`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Two-Factor Authentication (TOTP) - Models and Relations
class "auth_totp.device" as auth_totp_device
class Users
Users --|> auth_totp_device : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
