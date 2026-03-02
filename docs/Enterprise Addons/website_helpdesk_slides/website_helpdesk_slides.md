<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Website Slides Helpdesk

- Scope: Enterprise Addons
- Source: enterprise/website_helpdesk_slides
- Dependencies: [[docs/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]], [[docs/Community Addons/website_slides/website_slides|website_slides]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




