<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Snail Mail

- Version: v18
- Category: community
- Source: odoo/addons/snailmail
- Dependencies: [[Odoo 18/Community Addons/iap_mail/iap_mail|iap_mail]], [[Odoo 18/Community Addons/mail/mail|mail]]
## XML Artifacts (detected)

- Views: 4
- Actions: 3
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `IrActionsReport`
- `Message`
- `Notification`
- `Company`
- `ResPartner`
- `snailmail.letter`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Snail Mail - Models and Relations
class IrActionsReport
class Message
class Notification
class Company
class ResPartner
class "snailmail.letter" as snailmail_letter
Message --|> snailmail_letter : one2many
Notification --> snailmail_letter : many2one
class "res.users" as res_users
snailmail_letter --> res_users : many2one
class "res.partner" as res_partner
snailmail_letter --> res_partner : many2one
class "res.company" as res_company
snailmail_letter --> res_company : many2one
class "ir.actions.report" as ir_actions_report
snailmail_letter --> ir_actions_report : many2one
class "ir.attachment" as ir_attachment
snailmail_letter --> ir_attachment : many2one
class "mail.message" as mail_message
snailmail_letter --> mail_message : many2one
class "mail.notification" as mail_notification
snailmail_letter --|> mail_notification : one2many
class "res.country.state" as res_country_state
snailmail_letter --> res_country_state : many2one
class "res.country" as res_country
snailmail_letter --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
