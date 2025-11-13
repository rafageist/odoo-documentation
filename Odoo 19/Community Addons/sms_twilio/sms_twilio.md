<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Twilio SMS

- Version: v19
- Category: community
- Source: odoo19/addons/sms_twilio
- Dependencies: [[Odoo 19/Community Addons/sms/sms|sms]]

## Summary

Send SMS messages using Twilio

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `MailNotification`
- `ResCompany`
- `SmsSms`
- `SmsTracker`
- `sms.twilio.number`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Twilio SMS - Models and Relations
class MailNotification
class ResCompany
class SmsSms
class SmsTracker
class "sms.twilio.number" as sms_twilio_number
ResCompany --|> sms_twilio_number : one2many
class "res.company" as res_company
SmsSms --> res_company : many2one
sms_twilio_number --> res_company : many2one
class "res.country" as res_country
sms_twilio_number --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
