<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Website IM Livechat Helpdesk

- Version: v18
- Category: enterprise
- Source: enterprise18/website_helpdesk_livechat
- Dependencies: [[Odoo 18/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]], [[Odoo 18/Community Addons/website_livechat/website_livechat|website_livechat]]

## Summary

Ticketing, Support, Livechat

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ChatbotScript`
- `ChatbotScriptStep`
- `HelpdeskTeam`
- `DiscussChannel`
- `Users`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website IM Livechat Helpdesk - Models and Relations
class ChatbotScript
class ChatbotScriptStep
class HelpdeskTeam
class DiscussChannel
class Users
class "helpdesk.team" as helpdesk_team
ChatbotScriptStep --> helpdesk_team : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
