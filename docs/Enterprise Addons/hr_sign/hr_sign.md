
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Contract - Signature

- Scope: Enterprise Addons
- Source: enterprise/hr_sign
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Enterprise Addons/sign/sign|sign]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


