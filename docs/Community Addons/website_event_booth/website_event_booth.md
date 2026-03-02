
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Online Event Booths

- Scope: Community Addons
- Source: odoo/addons/website_event_booth
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]], [[docs/Community Addons/event_booth/event_booth|event_booth]]

## Summary

Events, display your booths on your website

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `EventEvent`
- `EventType`
- `WebsiteEventMenu`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Online Event Booths - Models and Relations
class EventEvent
class EventType
class WebsiteEventMenu
class "website.event.menu" as website_event_menu
EventEvent --|> website_event_menu : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

