<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Website Live Chat

- Version: v18
- Category: community
- Source: odoo/addons/website_livechat
- Dependencies: [[Odoo 18/Community Addons/website/website|website]], [[Odoo 18/Community Addons/im_livechat/im_livechat|im_livechat]]

## Summary

Chat with your website visitors

## XML Artifacts (detected)

- Views: 8
- Actions: 5
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 5

## Detected Models

- `ChatbotScript`
- `ChatbotScriptStep`
- `DiscussChannel`
- `im_livechat.channel`
- `ImLivechatChannel`
- `Website`
- `WebsiteVisitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Live Chat - Models and Relations
class ChatbotScript
class ChatbotScriptStep
class DiscussChannel
class "im_livechat.channel" as im_livechat_channel
class ImLivechatChannel
class Website
class WebsiteVisitor
class "website.visitor" as website_visitor
DiscussChannel --> website_visitor : many2one
Website --> im_livechat_channel : many2one
class "res.partner" as res_partner
WebsiteVisitor --> res_partner : many2one
class "discuss.channel" as discuss_channel
WebsiteVisitor --|> discuss_channel : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
