<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Tours

- Scope: Community Addons
- Source: odoo/addons/web_tour
- Dependencies: [[docs/Community Addons/web/web|web]]

## XML Artifacts (detected)

- Views: 3
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `ResUsers`
- `web_tour.tour`
- `web_tour.tour.step`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Tours - Models and Relations
class ResUsers
class "web_tour.tour" as web_tour_tour
class "web_tour.tour.step" as web_tour_tour_step
web_tour_tour --|> web_tour_tour_step : one2many
class "res.users" as res_users
web_tour_tour .. res_users : many2many
web_tour_tour_step --> web_tour_tour : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



