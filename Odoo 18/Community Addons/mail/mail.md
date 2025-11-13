<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Discuss

- Version: v18
- Category: community
- Source: odoo/addons/mail
- Dependencies: base (not documented), [[Odoo 18/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 18/Community Addons/bus/bus|bus]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 18/Community Addons/html_editor/html_editor|html_editor]]

## Summary

Chat, mail gateway and private channels

## XML Artifacts (detected)

- Views: 106
- Actions: 51
- Menus: 34
- Rules (ir.rule): 25
- Access CSV entries: 63

## Detected Models

- `BusPresence`
- `fetchmail.server`
- `ir.actions.server`
- `ActWindowView`
- `IrAttachment`
- `IrConfigParameter`
- `ir.mail_server`
- `IrModel`
- `IrModelField`
- `IrUiMenu`
- `View`
- `mail.activity`
- `mail.activity.plan`
- `mail.activity.plan.template`
- `mail.activity.type`
- `mail.alias`
- `mail.alias.domain`
- `mail.blacklist`
- `mail.canned.response`
- `mail.followers`
- `mail.gateway.allowed`
- `mail.ice.server`
- `mail.link.preview`
- `mail.mail`
- `mail.message`
- `mail.message.reaction`
- `mail.message.schedule`
- `mail.message.subtype`
- `mail.message.translation`
- `mail.notification`
- `mail.push`
- `mail.push.device`
- `mail.scheduled.message`
- `mail.template`
- `mail.tracking.value`
- `res.company`
- `res.partner`
- `res.users`
- `ResUsersSettings`
- `res.users.settings.volumes`
- `discuss.channel`
- `discuss.channel.member`
- `discuss.channel.rtc.session`
- `discuss.gif.favorite`
- `discuss.voice.metadata`
- `mail.guest`
- `MailMessage`
- `ResGroups`
- `ResPartner`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Discuss - Models and Relations
class BusPresence
class "fetchmail.server" as fetchmail_server
class "ir.actions.server" as ir_actions_server
class ActWindowView
class IrAttachment
class IrConfigParameter
class "ir.mail_server" as ir_mail_server
class IrModel
class IrModelField
class IrUiMenu
class View
class "mail.activity" as mail_activity
class "mail.activity.plan" as mail_activity_plan
class "mail.activity.plan.template" as mail_activity_plan_template
class "mail.activity.type" as mail_activity_type
class "mail.alias" as mail_alias
class "mail.alias.domain" as mail_alias_domain
class "mail.blacklist" as mail_blacklist
class "mail.canned.response" as mail_canned_response
class "mail.followers" as mail_followers
class "mail.gateway.allowed" as mail_gateway_allowed
class "mail.ice.server" as mail_ice_server
class "mail.link.preview" as mail_link_preview
class "mail.mail" as mail_mail
class "mail.message" as mail_message
class "mail.message.reaction" as mail_message_reaction
class "mail.message.schedule" as mail_message_schedule
class "mail.message.subtype" as mail_message_subtype
class "mail.message.translation" as mail_message_translation
class "mail.notification" as mail_notification
class "mail.push" as mail_push
class "mail.push.device" as mail_push_device
class "mail.scheduled.message" as mail_scheduled_message
class "mail.template" as mail_template
class "mail.tracking.value" as mail_tracking_value
class "res.company" as res_company
class "res.partner" as res_partner
class "res.users" as res_users
class ResUsersSettings
class "res.users.settings.volumes" as res_users_settings_volumes
class "discuss.channel" as discuss_channel
class "discuss.channel.member" as discuss_channel_member
class "discuss.channel.rtc.session" as discuss_channel_rtc_session
class "discuss.gif.favorite" as discuss_gif_favorite
class "discuss.voice.metadata" as discuss_voice_metadata
class "mail.guest" as mail_guest
class MailMessage
class ResGroups
class ResPartner
class ResUsers
BusPresence --> mail_guest : many2one
class "ir.model" as ir_model
fetchmail_server --> ir_model : many2one
fetchmail_server --|> mail_mail : one2many
ir_actions_server .. res_partner : many2many
ir_actions_server --> mail_template : many2one
ir_actions_server --> mail_activity_type : many2one
ir_actions_server --> res_users : many2one
ir_mail_server --|> mail_template : one2many
mail_activity --> ir_model : many2one
mail_activity --> mail_activity_type : many2one
class "ir.attachment" as ir_attachment
mail_activity .. ir_attachment : many2many
mail_activity --> res_users : many2one
mail_activity --> res_partner : many2one
mail_activity --> mail_activity_type : many2one
mail_activity --> mail_activity_type : many2one
mail_activity_plan --> res_company : many2one
mail_activity_plan --|> mail_activity_plan_template : one2many
mail_activity_plan --> ir_model : many2one
mail_activity_plan_template --> mail_activity_plan : many2one
mail_activity_plan_template --> mail_activity_type : many2one
mail_activity_plan_template --> res_users : many2one
mail_activity_type --> res_users : many2one
mail_activity_type --> mail_activity_type : many2one
mail_activity_type .. mail_activity_type : many2many
mail_activity_type .. mail_activity_type : many2many
mail_activity_type .. mail_template : many2many
mail_activity_type --> res_users : many2one
mail_alias --> mail_alias_domain : many2one
mail_alias --> ir_model : many2one
mail_alias --> ir_model : many2one
mail_alias_domain --|> res_company : one2many
class "res.groups" as res_groups
mail_canned_response .. res_groups : many2many
mail_followers --> res_partner : many2one
mail_followers .. mail_message_subtype : many2many
mail_link_preview --> mail_message : many2one
mail_mail --> mail_message : many2one
mail_mail .. ir_attachment : many2many
mail_mail .. res_partner : many2many
mail_mail --> fetchmail_server : many2one
mail_message --|> mail_link_preview : one2many
mail_message --|> mail_message_reaction : one2many
mail_message .. ir_attachment : many2many
mail_message --> mail_message : many2one
mail_message --|> mail_message : one2many
mail_message --> mail_alias_domain : many2one
mail_message --> res_company : many2one
mail_message --> mail_message_subtype : many2one
mail_message --> mail_activity_type : many2one
mail_message --> res_partner : many2one
mail_message --> mail_guest : many2one
mail_message .. res_partner : many2many
mail_message .. res_partner : many2many
mail_message --|> mail_notification : one2many
mail_message .. res_partner : many2many
mail_message --|> mail_tracking_value : one2many
mail_message --> ir_mail_server : many2one
mail_message --|> mail_mail : one2many
mail_message_reaction --> mail_message : many2one
mail_message_reaction --> res_partner : many2one
mail_message_reaction --> mail_guest : many2one
mail_message_schedule --> mail_message : many2one
mail_message_subtype --> mail_message_subtype : many2one
mail_message_translation --> mail_message : many2one
mail_notification --> res_partner : many2one
mail_notification --> mail_message : many2one
mail_notification --> mail_mail : many2one
mail_notification --> res_partner : many2one
mail_push --> mail_push_device : many2one
mail_push_device --> res_partner : many2one
mail_scheduled_message .. ir_attachment : many2many
mail_scheduled_message --> res_partner : many2one
mail_scheduled_message .. res_partner : many2many
mail_template --> ir_model : many2one
mail_template --> res_users : many2one
mail_template .. ir_attachment : many2many
class "ir.actions.report" as ir_actions_report
mail_template .. ir_actions_report : many2many
mail_template --> ir_mail_server : many2one
class "ir.actions.act_window" as ir_actions_act_window
mail_template --> ir_actions_act_window : many2one
class "ir.model.fields" as ir_model_fields
mail_tracking_value --> ir_model_fields : many2one
class "res.currency" as res_currency
mail_tracking_value --> res_currency : many2one
mail_tracking_value --> mail_message : many2one
res_company --> mail_alias_domain : many2one
res_partner .. mail_message : many2many
ResUsersSettings --|> res_users_settings_volumes : one2many
class "res.users.settings" as res_users_settings
res_users_settings_volumes --> res_users_settings : many2one
res_users_settings_volumes --> res_partner : many2one
res_users_settings_volumes --> res_partner : many2one
discuss_channel .. res_partner : many2many
discuss_channel --|> discuss_channel_member : one2many
discuss_channel --> discuss_channel : many2one
discuss_channel --|> discuss_channel : one2many
discuss_channel --> mail_message : many2one
discuss_channel --|> mail_message : one2many
discuss_channel --|> discuss_channel_rtc_session : one2many
discuss_channel .. res_groups : many2many
discuss_channel --> res_groups : many2one
discuss_channel_member --> res_partner : many2one
discuss_channel_member --> mail_guest : many2one
discuss_channel_member --> discuss_channel : many2one
discuss_channel_member --> mail_message : many2one
discuss_channel_member --> mail_message : many2one
discuss_channel_member --|> discuss_channel_rtc_session : one2many
discuss_channel_member --> discuss_channel_rtc_session : many2one
discuss_channel_rtc_session --> discuss_channel_member : many2one
discuss_channel_rtc_session --> discuss_channel : many2one
discuss_channel_rtc_session --> res_partner : many2one
discuss_channel_rtc_session --> mail_guest : many2one
discuss_voice_metadata --> ir_attachment : many2one
class "res.country" as res_country
mail_guest --> res_country : many2one
mail_guest .. discuss_channel : many2many
ResPartner .. discuss_channel : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
