<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Contract - Signature

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_contract_sign
- Dependencies: [[Odoo 18/Community Addons/hr_contract/hr_contract|hr_contract]], [[Odoo 18/Enterprise Addons/sign/sign|sign]]

## Summary

Manage your documents to sign in contracts

## XML Artifacts (detected)

- Views: 8
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `hr.contract`
- `hr.employee`
- `MailActivityPlanTemplate`
- `res.users`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Contract - Signature - Models and Relations
class "hr.contract" as hr_contract
class "hr.employee" as hr_employee
class MailActivityPlanTemplate
class "res.users" as res_users
class "sign.request" as sign_request
hr_contract .. sign_request : many2many
hr_employee .. sign_request : many2many
class "sign.template" as sign_template
MailActivityPlanTemplate --> sign_template : many2one
class "sign.item.role" as sign_item_role
MailActivityPlanTemplate --> sign_item_role : many2one
MailActivityPlanTemplate .. sign_item_role : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
