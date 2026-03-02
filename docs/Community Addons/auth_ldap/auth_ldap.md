<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Authentication via LDAP

- Scope: Community Addons
- Source: odoo/addons/auth_ldap
- Dependencies: base (not documented), [[docs/Community Addons/base_setup/base_setup|base_setup]]

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `ResCompany`
- `res.company.ldap`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Authentication via LDAP - Models and Relations
class ResCompany
class "res.company.ldap" as res_company_ldap
class ResUsers
ResCompany --|> res_company_ldap : one2many
class "res.company" as res_company
res_company_ldap --> res_company : many2one
class "res.users" as res_users
res_company_ldap --> res_users : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





