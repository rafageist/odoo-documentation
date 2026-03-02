<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Privacy

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/privacy_lookup
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 5
- Actions: 8
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `privacy.log`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Privacy - Models and Relations
class "privacy.log" as privacy_log
class ResPartner
class "res.users" as res_users
privacy_log --> res_users : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


