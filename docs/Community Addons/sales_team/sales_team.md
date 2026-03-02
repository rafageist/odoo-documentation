<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales Teams

- Scope: Community Addons
- Source: odoo/addons/sales_team
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]]

## Summary

Sales Teams

## XML Artifacts (detected)

- Views: 14
- Actions: 6
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 9

## Detected Models

- `crm.tag`
- `crm.team`
- `crm.team.member`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Sales Teams - Models and Relations
class "crm.tag" as crm_tag
class "crm.team" as crm_team
class "crm.team.member" as crm_team_member
class ResUsers
class "res.company" as res_company
crm_team --> res_company : many2one
class "res.currency" as res_currency
crm_team --> res_currency : many2one
class "res.users" as res_users
crm_team --> res_users : many2one
crm_team .. res_users : many2many
crm_team .. res_company : many2many
crm_team --|> crm_team_member : one2many
crm_team --|> crm_team_member : one2many
crm_team .. res_users : many2many
crm_team_member --> crm_team : many2one
crm_team_member --> res_users : many2one
crm_team_member .. res_users : many2many
crm_team_member .. res_company : many2many
crm_team_member --> res_company : many2one
ResUsers .. crm_team : many2many
ResUsers --|> crm_team_member : one2many
ResUsers --> crm_team : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




