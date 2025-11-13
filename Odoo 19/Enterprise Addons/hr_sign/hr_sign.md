<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Contract - Signature

- Version: v19
- Category: enterprise
- Source: enterprise19/hr_sign
- Dependencies: [[Odoo 19/Community Addons/hr/hr|hr]], [[Odoo 19/Enterprise Addons/sign/sign|sign]]

## Summary

Manage your documents to sign in contracts

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `HrEmployee`
- `HrEmployeePublic`
- `HrVersion`
- `MailActivityPlanTemplate`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Contract - Signature - Models and Relations
class HrEmployee
class HrEmployeePublic
class HrVersion
class MailActivityPlanTemplate
class ResUsers
class "sign.request" as sign_request
HrEmployee .. sign_request : many2many
HrEmployeePublic .. sign_request : many2many
HrVersion .. sign_request : many2many
class "sign.template" as sign_template
MailActivityPlanTemplate --> sign_template : many2one
class "sign.item.role" as sign_item_role
MailActivityPlanTemplate --> sign_item_role : many2one
MailActivityPlanTemplate .. sign_item_role : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
