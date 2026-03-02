<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Tours

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/web_tour
- Dependencies: [[Odoo 19/Community Addons/web/web|web]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

