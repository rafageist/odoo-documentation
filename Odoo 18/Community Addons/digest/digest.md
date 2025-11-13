<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# KPI Digests

- Version: v18
- Category: community
- Source: odoo/addons/digest
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/resource/resource|resource]]
## XML Artifacts (detected)

- Views: 7
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `digest.digest`
- `digest.tip`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title KPI Digests - Models and Relations
class "digest.digest" as digest_digest
class "digest.tip" as digest_tip
class ResUsers
class "res.users" as res_users
digest_digest .. res_users : many2many
class "res.company" as res_company
digest_digest --> res_company : many2one
digest_tip .. res_users : many2many
class "res.groups" as res_groups
digest_tip --> res_groups : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
