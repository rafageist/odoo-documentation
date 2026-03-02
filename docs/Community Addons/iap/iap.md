<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# In-App Purchases

- Scope: Community Addons
- Source: odoo/addons/iap
- Dependencies: [[docs/Community Addons/web/web|web]], [[docs/Community Addons/base_setup/base_setup|base_setup]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





