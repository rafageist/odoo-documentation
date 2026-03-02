<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Privacy

- Scope: Community Addons
- Source: odoo/addons/privacy_lookup
- Dependencies: [[docs/Community Addons/mail/mail|mail]]

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
!include ../../../templates/DiagramStyles.puml
title Privacy - Models and Relations
class "privacy.log" as privacy_log
class ResPartner
class "res.users" as res_users
privacy_log --> res_users : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





