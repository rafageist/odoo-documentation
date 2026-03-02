<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# WhatsApp Follow-Up

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/whatsapp_account_followup
- Dependencies: [[Odoo 19/Enterprise Addons/account_followup/account_followup|account_followup]], [[Odoo 19/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

## Summary

Send Follow-Up to your Contacts on WhatsApp

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Account_FollowupFollowupLine`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title WhatsApp Follow-Up - Models and Relations
class Account_FollowupFollowupLine
class ResPartner
class "whatsapp.template" as whatsapp_template
Account_FollowupFollowupLine --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

