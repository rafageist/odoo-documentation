<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Live Chat

- Version: v18
- Category: community
- Source: odoo/addons/im_livechat
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/rating/rating|rating]], [[Odoo 18/Community Addons/digest/digest|digest]], [[Odoo 18/Community Addons/utm/utm|utm]]

## Summary

Chat with your website visitors

## XML Artifacts (detected)

- Views: 29
- Actions: 20
- Menus: 10
- Rules (ir.rule): 2
- Access CSV entries: 17

## Detected Models

- `chatbot.message`
- `chatbot.script`
- `chatbot.script.answer`
- `chatbot.script.step`
- `Digest`
- `discuss.channel`
- `ChannelMember`
- `im_livechat.channel`
- `im_livechat.channel.rule`
- `MailMessage`
- `Rating`
- `Partners`
- `Users`
- `ResUsersSettings`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Live Chat - Models and Relations
class "chatbot.message" as chatbot_message
class "chatbot.script" as chatbot_script
class "chatbot.script.answer" as chatbot_script_answer
class "chatbot.script.step" as chatbot_script_step
class Digest
class "discuss.channel" as discuss_channel
class ChannelMember
class "im_livechat.channel" as im_livechat_channel
class "im_livechat.channel.rule" as im_livechat_channel_rule
class MailMessage
class Rating
class Partners
class Users
class ResUsersSettings
class "mail.message" as mail_message
chatbot_message --> mail_message : many2one
chatbot_message --> discuss_channel : many2one
chatbot_message --> chatbot_script_step : many2one
chatbot_message --> chatbot_script_answer : many2one
chatbot_script --|> chatbot_script_step : one2many
class "res.partner" as res_partner
chatbot_script --> res_partner : many2one
chatbot_script_answer --> chatbot_script_step : many2one
chatbot_script_step --> chatbot_script : many2one
chatbot_script_step --|> chatbot_script_answer : one2many
chatbot_script_step .. chatbot_script_answer : many2many
discuss_channel --> im_livechat_channel : many2one
discuss_channel --> res_partner : many2one
discuss_channel --> chatbot_script_step : many2one
discuss_channel --|> chatbot_message : one2many
class "res.country" as res_country
discuss_channel --> res_country : many2one
class "res.users" as res_users
im_livechat_channel .. res_users : many2many
im_livechat_channel .. res_users : many2many
im_livechat_channel --|> discuss_channel : one2many
im_livechat_channel --|> im_livechat_channel_rule : one2many
im_livechat_channel_rule --> chatbot_script : many2one
im_livechat_channel_rule --> im_livechat_channel : many2one
im_livechat_channel_rule .. res_country : many2many
class "res.lang" as res_lang
Users .. res_lang : many2many
ResUsersSettings .. res_lang : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
