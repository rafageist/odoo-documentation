<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Website Jitsi

- Version: v18
- Category: community
- Source: odoo/addons/website_jitsi
- Dependencies: [[Odoo 18/Community Addons/website/website|website]]

## Summary

Create Jitsi room on website.

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `chat.room`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Jitsi - Models and Relations
class "chat.room" as chat_room
class "res.lang" as res_lang
chat_room --> res_lang : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
