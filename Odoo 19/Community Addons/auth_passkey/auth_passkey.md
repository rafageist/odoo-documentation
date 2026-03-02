<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Passkeys

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/auth_passkey
- Dependencies: [[Odoo 19/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 19/Community Addons/web/web|web]]

## Summary

Log in with a Passkey

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 3
- Access CSV entries: 5

## Detected Models

- `auth.passkey.key`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Passkeys - Models and Relations
class "auth.passkey.key" as auth_passkey_key
class ResUsers
class "res.users" as res_users
auth_passkey_key --> res_users : many2one
ResUsers --|> auth_passkey_key : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


