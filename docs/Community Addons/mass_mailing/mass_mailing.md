<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Email Marketing

- Scope: Community Addons
- Source: odoo/addons/mass_mailing
- Dependencies: [[docs/Community Addons/contacts/contacts|contacts]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/html_builder/html_builder|html_builder]], [[docs/Community Addons/utm/utm|utm]], [[docs/Community Addons/link_tracker/link_tracker|link_tracker]], [[docs/Community Addons/social_media/social_media|social_media]], [[docs/Community Addons/web_tour/web_tour|web_tour]], [[docs/Community Addons/digest/digest|digest]]

## Summary

Design, send and track emails

## XML Artifacts (detected)

- Views: 57
- Actions: 22
- Menus: 19
- Rules (ir.rule): 1
- Access CSV entries: 25

## Detected Models

- `IrMail_Server`
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
- `MailBlacklist`
- `MailMail`
- `ResCompany`
- `ResPartner`
- `ResUsers`
- `UtmCampaign`
- `UtmMedium`
- `UtmSource`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Email Marketing - Models and Relations
class IrMail_Server
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
class MailBlacklist
class MailMail
class ResCompany
class ResPartner
class ResUsers
class UtmCampaign
class UtmMedium
class UtmSource
IrMail_Server --|> mailing_mailing : one2many
LinkTracker --> mailing_mailing : many2one
LinkTrackerClick --> mailing_trace : many2one
LinkTrackerClick --> mailing_mailing : many2one
class "ir.attachment" as ir_attachment
mailing_mailing .. ir_attachment : many2many
class "utm.campaign" as utm_campaign
mailing_mailing --> utm_campaign : many2one
class "utm.medium" as utm_medium
mailing_mailing --> utm_medium : many2one
class "res.users" as res_users
mailing_mailing --> res_users : many2one
class "ir.model" as ir_model
mailing_mailing --> ir_model : many2one
class "ir.mail_server" as ir_mail_server
mailing_mailing --> ir_mail_server : many2one
mailing_mailing .. mailing_list : many2many
mailing_mailing --> mailing_filter : many2one
mailing_mailing --|> mailing_trace : one2many
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
MailBlacklist --> mailing_subscription_optout : many2one
MailMail --> mailing_mailing : many2one
MailMail --|> mailing_trace : one2many
UtmCampaign --|> mailing_mailing : one2many
UtmCampaign --> mailing_mailing : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





