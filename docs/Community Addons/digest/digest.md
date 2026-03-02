<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# KPI Digests

- Scope: Community Addons
- Source: odoo/addons/digest
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/resource/resource|resource]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





