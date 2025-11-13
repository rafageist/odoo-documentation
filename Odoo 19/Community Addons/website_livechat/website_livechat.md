<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Website Live Chat

- Version: v19
- Category: community
- Source: odoo19/addons/website_livechat
- Dependencies: [[Odoo 19/Community Addons/website/website|website]], [[Odoo 19/Community Addons/im_livechat/im_livechat|im_livechat]]

## Summary

Chat with your website visitors

## XML Artifacts (detected)

- Views: 7
- Actions: 5
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `ChatbotScript`
- `ChatbotScriptStep`
- `DiscussChannel`
- `Im_LivechatChannel`
- `Website`
- `WebsiteVisitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Live Chat - Models and Relations
class ChatbotScript
class ChatbotScriptStep
class DiscussChannel
class Im_LivechatChannel
class Website
class WebsiteVisitor
class "website.visitor" as website_visitor
DiscussChannel --> website_visitor : many2one
class "im_livechat.channel" as im_livechat_channel
Website --> im_livechat_channel : many2one
class "res.partner" as res_partner
WebsiteVisitor --> res_partner : many2one
class "discuss.channel" as discuss_channel
WebsiteVisitor --|> discuss_channel : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
