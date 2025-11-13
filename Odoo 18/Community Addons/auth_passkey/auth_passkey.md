<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Passkeys

- Version: v18
- Category: community
- Source: odoo/addons/auth_passkey
- Dependencies: [[Odoo 18/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 18/Community Addons/web/web|web]]

## Summary

Log in with a Passkey

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 3

## Detected Models

- `auth.passkey.key`
- `UsersPasskey`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Passkeys - Models and Relations
class "auth.passkey.key" as auth_passkey_key
class UsersPasskey
UsersPasskey --|> auth_passkey_key : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
