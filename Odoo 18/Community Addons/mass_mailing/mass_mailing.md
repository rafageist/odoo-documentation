<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Email Marketing

- Version: v18
- Category: community
- Source: odoo/addons/mass_mailing
- Dependencies: [[Odoo 18/Community Addons/contacts/contacts|contacts]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/utm/utm|utm]], [[Odoo 18/Community Addons/link_tracker/link_tracker|link_tracker]], [[Odoo 18/Community Addons/web_editor/web_editor|web_editor]], [[Odoo 18/Community Addons/social_media/social_media|social_media]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 18/Community Addons/digest/digest|digest]]

## Summary

Design, send and track emails

## XML Artifacts (detected)

- Views: 56
- Actions: 22
- Menus: 19
- Rules (ir.rule): 0
- Access CSV entries: 25

## Detected Models

- `ir.mail_server`
- `IrModel`
- `LinkTracker`
- `LinkTrackerClick`
- `mailing.mailing`
- `mailing.contact`
- `mailing.filter`
- `mailing.list`
- `mailing.subscription`
- `mailing.subscription.optout`
- `mailing.trace`
- `MailBlackList`
- `MailMail`
- `ResCompany`
- `Partner`
- `res.users`
- `UtmCampaign`
- `UtmMedium`
- `UtmSource`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Email Marketing - Models and Relations
class "ir.mail_server" as ir_mail_server
class IrModel
class LinkTracker
class LinkTrackerClick
class "mailing.mailing" as mailing_mailing
class "mailing.contact" as mailing_contact
class "mailing.filter" as mailing_filter
class "mailing.list" as mailing_list
class "mailing.subscription" as mailing_subscription
class "mailing.subscription.optout" as mailing_subscription_optout
class "mailing.trace" as mailing_trace
class MailBlackList
class MailMail
class ResCompany
class Partner
class "res.users" as res_users
class UtmCampaign
class UtmMedium
class UtmSource
ir_mail_server --|> mailing_mailing : one2many
LinkTracker --> mailing_mailing : many2one
LinkTrackerClick --> mailing_trace : many2one
LinkTrackerClick --> mailing_mailing : many2one
class "ir.attachment" as ir_attachment
mailing_mailing .. ir_attachment : many2many
class "utm.campaign" as utm_campaign
mailing_mailing --> utm_campaign : many2one
class "utm.medium" as utm_medium
mailing_mailing --> utm_medium : many2one
mailing_mailing --> res_users : many2one
class "ir.model" as ir_model
mailing_mailing --> ir_model : many2one
mailing_mailing --> ir_mail_server : many2one
mailing_mailing .. mailing_list : many2many
mailing_mailing --> mailing_filter : many2one
mailing_mailing --|> mailing_trace : one2many
class "res.partner.title" as res_partner_title
mailing_contact --> res_partner_title : many2one
mailing_contact .. mailing_list : many2many
mailing_contact --|> mailing_subscription : one2many
class "res.country" as res_country
mailing_contact --> res_country : many2one
class "res.partner.category" as res_partner_category
mailing_contact .. res_partner_category : many2many
mailing_filter --> res_users : many2one
mailing_filter --> ir_model : many2one
mailing_list .. mailing_contact : many2many
mailing_list .. mailing_mailing : many2many
mailing_list --|> mailing_subscription : one2many
mailing_subscription --> mailing_contact : many2one
mailing_subscription --> mailing_list : many2one
mailing_subscription --> mailing_subscription_optout : many2one
class "mail.mail" as mail_mail
mailing_trace --> mail_mail : many2one
mailing_trace --> mailing_mailing : many2one
class "link.tracker.click" as link_tracker_click
mailing_trace --|> link_tracker_click : one2many
MailBlackList --> mailing_subscription_optout : many2one
MailMail --> mailing_mailing : many2one
MailMail --|> mailing_trace : one2many
UtmCampaign --|> mailing_mailing : one2many
UtmCampaign --> mailing_mailing : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
