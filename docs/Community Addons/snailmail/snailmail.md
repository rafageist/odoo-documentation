<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Snail Mail

- Scope: Community Addons
- Source: odoo/addons/snailmail
- Dependencies: [[docs/Community Addons/iap_mail/iap_mail|iap_mail]], [[docs/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `IrActionsReport`
- `MailMessage`
- `MailNotification`
- `ResCompany`
- `ResPartner`
- `snailmail.letter`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Snail Mail - Models and Relations
class IrActionsReport
class MailMessage
class MailNotification
class ResCompany
class ResPartner
class "snailmail.letter" as snailmail_letter
MailMessage --|> snailmail_letter : one2many
MailNotification --> snailmail_letter : many2one
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




