<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# IAP / Mail

- Version: v18
- Category: community
- Source: odoo/addons/iap_mail
- Dependencies: [[Odoo 18/Community Addons/iap/iap|iap]], [[Odoo 18/Community Addons/mail/mail|mail]]

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
!include ../../../Templates/DiagramStyles.puml
title IAP / Mail - Models and Relations
class "iap.account" as iap_account
class "res.company" as res_company
iap_account .. res_company : many2many
class "res.users" as res_users
iap_account .. res_users : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
