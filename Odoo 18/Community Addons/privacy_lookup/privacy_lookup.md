<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Privacy

- Version: v18
- Category: community
- Source: odoo/addons/privacy_lookup
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]]
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
