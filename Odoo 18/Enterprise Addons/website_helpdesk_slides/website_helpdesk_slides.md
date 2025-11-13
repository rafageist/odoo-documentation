<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Website Slides Helpdesk

- Version: v18
- Category: enterprise
- Source: enterprise18/website_helpdesk_slides
- Dependencies: [[Odoo 18/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]], [[Odoo 18/Community Addons/website_slides/website_slides|website_slides]]

## Summary

Ticketing, Support, Slides

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HelpdeskTeam`
- `SlideChannel`
- `SlideSlide`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Slides Helpdesk - Models and Relations
class HelpdeskTeam
class SlideChannel
class SlideSlide
class "slide.channel" as slide_channel
HelpdeskTeam .. slide_channel : many2many
HelpdeskTeam .. slide_channel : many2many
class "helpdesk.team" as helpdesk_team
SlideChannel .. helpdesk_team : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
