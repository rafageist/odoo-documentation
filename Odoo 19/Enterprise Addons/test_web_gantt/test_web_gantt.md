<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Web Gantt Tests

- Version: v19
- Category: enterprise
- Source: enterprise19/test_web_gantt
- Dependencies: [[Odoo 19/Enterprise Addons/web_gantt/web_gantt|web_gantt]]

## Summary

Web Gantt Tests: Tests specific to the gantt view

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `test.web.gantt.pill`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Web Gantt Tests - Models and Relations
class "test.web.gantt.pill" as test_web_gantt_pill
test_web_gantt_pill .. test_web_gantt_pill : many2many
test_web_gantt_pill .. test_web_gantt_pill : many2many
test_web_gantt_pill --> test_web_gantt_pill : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
