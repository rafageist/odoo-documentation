<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Payment Follow-up Management

- Scope: Enterprise Addons
- Source: enterprise/account_followup
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/sms/sms|sms]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## XML Artifacts (detected)

- Views: 11
- Actions: 5
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 7

## Detected Models

- `account_followup.followup.line`
- `AccountMoveLine`
- `IrActionsReport`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Payment Follow-up Management - Models and Relations
class "account_followup.followup.line" as account_followup_followup_line
class AccountMoveLine
class IrActionsReport
class ResPartner
class "res.company" as res_company
account_followup_followup_line --> res_company : many2one
class "mail.template" as mail_template
account_followup_followup_line --> mail_template : many2one
class "res.users" as res_users
account_followup_followup_line .. res_users : many2many
class "sms.template" as sms_template
account_followup_followup_line --> sms_template : many2one
class "mail.activity.type" as mail_activity_type
account_followup_followup_line --> mail_activity_type : many2one
AccountMoveLine --> account_followup_followup_line : many2one
class "account.move.line" as account_move_line
ResPartner --|> account_move_line : one2many
class "account.move" as account_move
ResPartner --|> account_move : one2many
ResPartner --> account_followup_followup_line : many2one
ResPartner --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




