<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# KPI Digests

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/digest
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Community Addons/resource/resource|resource]]

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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


