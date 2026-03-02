<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Live Chat

- Scope: Community Addons
- Source: odoo/addons/im_livechat
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/rating/rating|rating]], [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/utm/utm|utm]]

## Summary

Chat with your website visitors

## XML Artifacts (detected)

- Views: 40
- Actions: 25
- Menus: 15
- Rules (ir.rule): 3
- Access CSV entries: 15

## Detected Models

- `chatbot.message`
- `chatbot.script`
- `chatbot.script.answer`
- `chatbot.script.step`
- `DigestDigest`
- `DiscussCallHistory`
- `discuss.channel`
- `DiscussChannelMember`
- `DiscussChannelRtcSession`
- `im_livechat.channel`
- `im_livechat.channel.rule`
- `im_livechat.channel.member.history`
- `im_livechat.conversation.tag`
- `im_livechat.expertise`
- `MailMessage`
- `RatingRating`
- `ResGroups`
- `ResPartner`
- `ResUsers`
- `ResUsersSettings`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Live Chat - Models and Relations
class "chatbot.message" as chatbot_message
class "chatbot.script" as chatbot_script
class "chatbot.script.answer" as chatbot_script_answer
class "chatbot.script.step" as chatbot_script_step
class DigestDigest
class DiscussCallHistory
class "discuss.channel" as discuss_channel
class DiscussChannelMember
class DiscussChannelRtcSession
class "im_livechat.channel" as im_livechat_channel
class "im_livechat.channel.rule" as im_livechat_channel_rule
class "im_livechat.channel.member.history" as im_livechat_channel_member_history
class "im_livechat.conversation.tag" as im_livechat_conversation_tag
class "im_livechat.expertise" as im_livechat_expertise
class MailMessage
class RatingRating
class ResGroups
class ResPartner
class ResUsers
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
chatbot_script_step .. im_livechat_expertise : many2many
DiscussCallHistory .. im_livechat_channel_member_history : many2many
class "res.lang" as res_lang
discuss_channel --> res_lang : many2one
discuss_channel --> im_livechat_channel : many2one
discuss_channel --> res_partner : many2one
discuss_channel --|> im_livechat_channel_member_history : one2many
discuss_channel .. im_livechat_expertise : many2many
discuss_channel --|> im_livechat_channel_member_history : one2many
discuss_channel --|> im_livechat_channel_member_history : one2many
discuss_channel --|> im_livechat_channel_member_history : one2many
discuss_channel .. res_partner : many2many
discuss_channel .. res_partner : many2many
discuss_channel .. res_partner : many2many
class "mail.guest" as mail_guest
discuss_channel .. mail_guest : many2many
discuss_channel --> im_livechat_channel_member_history : many2one
discuss_channel --> im_livechat_channel_member_history : many2one
discuss_channel .. im_livechat_conversation_tag : many2many
discuss_channel --> chatbot_script_step : many2one
discuss_channel --|> chatbot_message : one2many
class "res.country" as res_country
discuss_channel --> res_country : many2one
DiscussChannelMember --|> im_livechat_channel_member_history : one2many
DiscussChannelMember --> chatbot_script : many2one
DiscussChannelMember .. im_livechat_expertise : many2many
class "res.users" as res_users
im_livechat_channel .. res_users : many2many
im_livechat_channel .. res_users : many2many
im_livechat_channel --|> discuss_channel : one2many
im_livechat_channel --|> im_livechat_channel_rule : one2many
im_livechat_channel_rule --> chatbot_script : many2one
im_livechat_channel_rule --> im_livechat_channel : many2one
im_livechat_channel_rule .. res_country : many2many
class "discuss.channel.member" as discuss_channel_member
im_livechat_channel_member_history --> discuss_channel_member : many2one
im_livechat_channel_member_history --> discuss_channel : many2one
im_livechat_channel_member_history --> mail_guest : many2one
im_livechat_channel_member_history --> res_partner : many2one
im_livechat_channel_member_history --> chatbot_script : many2one
im_livechat_channel_member_history .. im_livechat_expertise : many2many
im_livechat_channel_member_history .. im_livechat_conversation_tag : many2many
im_livechat_channel_member_history --> res_country : many2one
im_livechat_channel_member_history --> im_livechat_channel : many2one
class "rating.rating" as rating_rating
im_livechat_channel_member_history --> rating_rating : many2one
class "discuss.call.history" as discuss_call_history
im_livechat_channel_member_history .. discuss_call_history : many2many
im_livechat_conversation_tag .. discuss_channel : many2many
im_livechat_expertise .. res_users : many2many
ResPartner --|> chatbot_script : one2many
ResUsers .. im_livechat_channel : many2many
ResUsers .. res_lang : many2many
ResUsers .. im_livechat_expertise : many2many
ResUsersSettings .. res_lang : many2many
ResUsersSettings .. im_livechat_expertise : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





