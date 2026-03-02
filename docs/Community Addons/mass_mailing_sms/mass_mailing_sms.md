<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# SMS Marketing

- Scope: Community Addons
- Source: odoo/addons/mass_mailing_sms
- Dependencies: [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[docs/Community Addons/sms/sms|sms]]

## Summary

Design, send and track SMS

## XML Artifacts (detected)

- Views: 23
- Actions: 10
- Menus: 10
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `mailing.contact`
- `MailingList`
- `MailingMailing`
- `MailingTrace`
- `ResUsers`
- `SmsSms`
- `SmsTracker`
- `UtmCampaign`
- `UtmMedium`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title SMS Marketing - Models and Relations
class "mailing.contact" as mailing_contact
class MailingList
class MailingMailing
class MailingTrace
class ResUsers
class SmsSms
class SmsTracker
class UtmCampaign
class UtmMedium
class "sms.template" as sms_template
MailingMailing --> sms_template : many2one
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





