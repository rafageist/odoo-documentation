<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Booths/Exhibitors Bridge

- Scope: Community Addons
- Source: odoo/addons/website_event_booth_exhibitor
- Dependencies: [[docs/Community Addons/website_event_exhibitor/website_event_exhibitor|website_event_exhibitor]], [[docs/Community Addons/website_event_booth/website_event_booth|website_event_booth]]

## Summary

Event Booths, automatically create a sponsor.

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `EventBooth`
- `EventBoothCategory`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Booths/Exhibitors Bridge - Models and Relations
class EventBooth
class EventBoothCategory
class "event.sponsor" as event_sponsor
EventBooth --> event_sponsor : many2one
class "event.sponsor.type" as event_sponsor_type
EventBoothCategory --> event_sponsor_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



