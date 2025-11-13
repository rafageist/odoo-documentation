<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Frontdesk

- Version: v18
- Category: enterprise
- Source: enterprise18/frontdesk
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/sms/sms|sms]]

## Summary

Visitor management system

## XML Artifacts (detected)

- Views: 19
- Actions: 14
- Menus: 9
- Rules (ir.rule): 6
- Access CSV entries: 7

## Detected Models

- `frontdesk.drink`
- `frontdesk.frontdesk`
- `frontdesk.visitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Frontdesk - Models and Relations
class "frontdesk.drink" as frontdesk_drink
class "frontdesk.frontdesk" as frontdesk_frontdesk
class "frontdesk.visitor" as frontdesk_visitor
class "res.users" as res_users
frontdesk_drink .. res_users : many2many
frontdesk_frontdesk .. res_users : many2many
class "res.company" as res_company
frontdesk_frontdesk --> res_company : many2one
class "mail.template" as mail_template
frontdesk_frontdesk --> mail_template : many2one
class "sms.template" as sms_template
frontdesk_frontdesk --> sms_template : many2one
frontdesk_frontdesk .. frontdesk_drink : many2many
frontdesk_frontdesk --|> frontdesk_visitor : one2many
class "hr.employee" as hr_employee
frontdesk_visitor .. hr_employee : many2many
frontdesk_visitor .. frontdesk_drink : many2many
frontdesk_visitor --> frontdesk_frontdesk : many2one
frontdesk_visitor --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
