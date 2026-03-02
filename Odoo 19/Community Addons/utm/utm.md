<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# UTM Trackers

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/utm
- Dependencies: base (not documented), [[Odoo 19/Community Addons/web/web|web]]

## XML Artifacts (detected)

- Views: 14
- Actions: 5
- Menus: 5
- Rules (ir.rule): 0
- Access CSV entries: 10

## Detected Models

- `utm.campaign`
- `utm.medium`
- `utm.source`
- `utm.stage`
- `utm.tag`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title UTM Trackers - Models and Relations
class "utm.campaign" as utm_campaign
class "utm.medium" as utm_medium
class "utm.source" as utm_source
class "utm.stage" as utm_stage
class "utm.tag" as utm_tag
class "res.users" as res_users
utm_campaign --> res_users : many2one
utm_campaign --> utm_stage : many2one
utm_campaign .. utm_tag : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

