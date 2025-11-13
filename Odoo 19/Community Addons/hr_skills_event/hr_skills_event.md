<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Skills Events

- Version: v19
- Category: community
- Source: odoo19/addons/hr_skills_event
- Dependencies: [[Odoo 19/Community Addons/hr_skills/hr_skills|hr_skills]], [[Odoo 19/Community Addons/event/event|event]]

## Summary

Link training events to resume of your employees

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrResumeLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Skills Events - Models and Relations
class HrResumeLine
class "event.event" as event_event
HrResumeLine --> event_event : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
