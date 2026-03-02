<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# WhatsApp Follow-Up

- Scope: Enterprise Addons
- Source: enterprise/whatsapp_account_followup
- Dependencies: [[docs/Enterprise Addons/account_followup/account_followup|account_followup]], [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

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
!include ../../../templates/DiagramStyles.puml
title WhatsApp Follow-Up - Models and Relations
class Account_FollowupFollowupLine
class ResPartner
class "whatsapp.template" as whatsapp_template
Account_FollowupFollowupLine --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




