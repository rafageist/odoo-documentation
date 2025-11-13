<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# SMS Marketing

- Version: v18
- Category: community
- Source: odoo/addons/mass_mailing_sms
- Dependencies: [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[Odoo 18/Community Addons/sms/sms|sms]]

## Summary

Design, send and track SMS

## XML Artifacts (detected)

- Views: 23
- Actions: 10
- Menus: 10
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `mailing.contact`
- `MailingList`
- `Mailing`
- `MailingTrace`
- `res.users`
- `SmsSms`
- `SmsTracker`
- `UtmCampaign`
- `UtmMedium`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title SMS Marketing - Models and Relations
class "mailing.contact" as mailing_contact
class MailingList
class Mailing
class MailingTrace
class "res.users" as res_users
class SmsSms
class SmsTracker
class UtmCampaign
class UtmMedium
class "sms.template" as sms_template
Mailing --> sms_template : many2one
class "sms.sms" as sms_sms
MailingTrace --> sms_sms : many2one
class "sms.tracker" as sms_tracker
MailingTrace --|> sms_tracker : one2many
class "mailing.mailing" as mailing_mailing
SmsSms --> mailing_mailing : many2one
class "mailing.trace" as mailing_trace
SmsSms --|> mailing_trace : one2many
SmsTracker --> mailing_trace : many2one
UtmCampaign --|> mailing_mailing : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
