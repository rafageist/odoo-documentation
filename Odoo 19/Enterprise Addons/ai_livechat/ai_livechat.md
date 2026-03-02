<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# AI Livechat

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/ai_livechat
- Dependencies: [[Odoo 19/Enterprise Addons/ai_app/ai_app|ai_app]], [[Odoo 19/Community Addons/im_livechat/im_livechat|im_livechat]]

## Summary


        Augment Livechat with AI Agents.
    

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AIAgent`
- `DiscussChannel`
- `DiscussChannelMember`
- `Im_LivechatChannel`
- `ImLivechatChannelMemberHistory`
- `Im_LivechatChannelRule`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title AI Livechat - Models and Relations
class AIAgent
class DiscussChannel
class DiscussChannelMember
class Im_LivechatChannel
class ImLivechatChannelMemberHistory
class Im_LivechatChannelRule
class "im_livechat.channel.rule" as im_livechat_channel_rule
AIAgent --|> im_livechat_channel_rule : one2many
class "ai.agent" as ai_agent
DiscussChannelMember --> ai_agent : many2one
ImLivechatChannelMemberHistory --> ai_agent : many2one
class "chatbot.script" as chatbot_script
Im_LivechatChannelRule --> chatbot_script : many2one
Im_LivechatChannelRule --> ai_agent : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

