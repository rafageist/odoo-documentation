<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# IAP / Mail

- Scope: Community Addons
- Source: odoo/addons/iap_mail
- Dependencies: [[docs/Community Addons/iap/iap|iap]], [[docs/Community Addons/mail/mail|mail]]

## Summary

Bridge between IAP and mail

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `iap.account`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title IAP / Mail - Models and Relations
class "iap.account" as iap_account
class "res.company" as res_company
iap_account .. res_company : many2many
class "res.users" as res_users
iap_account .. res_users : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





