<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# UTM Trackers

- Scope: Community Addons
- Source: odoo/addons/utm
- Dependencies: base (not documented), [[docs/Community Addons/web/web|web]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



