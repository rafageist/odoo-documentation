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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





