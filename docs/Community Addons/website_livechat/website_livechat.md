<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Website Live Chat

- Scope: Community Addons
- Source: odoo/addons/website_livechat
- Dependencies: [[docs/Community Addons/website/website|website]], [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



