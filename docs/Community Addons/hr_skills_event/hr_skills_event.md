<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Skills Events

- Scope: Community Addons
- Source: odoo/addons/hr_skills_event
- Dependencies: [[docs/Community Addons/hr_skills/hr_skills|hr_skills]], [[docs/Community Addons/event/event|event]]

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
!include ../../../templates/DiagramStyles.puml
title Skills Events - Models and Relations
class HrResumeLine
class "event.event" as event_event
HrResumeLine --> event_event : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





