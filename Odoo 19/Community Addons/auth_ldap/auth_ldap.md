<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Authentication via LDAP

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/auth_ldap
- Dependencies: base (not documented), [[Odoo 19/Community Addons/base_setup/base_setup|base_setup]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


