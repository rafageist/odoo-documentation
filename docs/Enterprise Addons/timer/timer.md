<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Timer

- Scope: Enterprise Addons
- Source: enterprise/timer
- Dependencies: [[docs/Community Addons/web/web|web]], [[docs/Community Addons/mail/mail|mail]]

## Summary

Record time

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 1

## Detected Models

- `timer.timer`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Timer - Models and Relations
class "timer.timer" as timer_timer
class "res.users" as res_users
timer_timer --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



