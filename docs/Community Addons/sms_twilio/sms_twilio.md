<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Twilio SMS

- Scope: Community Addons
- Source: odoo/addons/sms_twilio
- Dependencies: [[docs/Community Addons/sms/sms|sms]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




