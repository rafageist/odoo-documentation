<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Website IM Livechat Helpdesk

- Version: v19
- Category: enterprise
- Source: enterprise19/website_helpdesk_livechat
- Dependencies: [[Odoo 19/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]], [[Odoo 19/Community Addons/website_livechat/website_livechat|website_livechat]]

## Summary

Ticketing, Support, Livechat

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 0

## Detected Models

- `ChatbotScript`
- `ChatbotScriptStep`
- `DiscussChannel`
- `HelpdeskTeam`
- `HelpdeskTicket`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website IM Livechat Helpdesk - Models and Relations
class ChatbotScript
class ChatbotScriptStep
class DiscussChannel
class HelpdeskTeam
class HelpdeskTicket
class ResUsers
class "helpdesk.team" as helpdesk_team
ChatbotScriptStep --> helpdesk_team : many2one
class "helpdesk.ticket" as helpdesk_ticket
DiscussChannel --|> helpdesk_ticket : one2many
class "discuss.channel" as discuss_channel
HelpdeskTicket --> discuss_channel : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
