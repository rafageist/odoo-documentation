<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Timer

- Version: v18
- Category: enterprise
- Source: enterprise18/timer
- Dependencies: [[Odoo 18/Community Addons/web/web|web]], [[Odoo 18/Community Addons/mail/mail|mail]]

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
!include ../../../Templates/DiagramStyles.puml
title Timer - Models and Relations
class "timer.timer" as timer_timer
class "res.users" as res_users
timer_timer --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
