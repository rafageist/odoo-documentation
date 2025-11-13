<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# In-App Purchases

- Version: v19
- Category: community
- Source: odoo19/addons/iap
- Dependencies: [[Odoo 19/Community Addons/web/web|web]], [[Odoo 19/Community Addons/base_setup/base_setup|base_setup]]

## Summary

Basic models and helpers to support In-App purchases.

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `iap.account`
- `iap.service`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title In-App Purchases - Models and Relations
class "iap.account" as iap_account
class "iap.service" as iap_service
iap_account --> iap_service : many2one
class "res.company" as res_company
iap_account .. res_company : many2many
class "res.users" as res_users
iap_account .. res_users : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
