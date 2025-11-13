<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgian Registered Cash Register

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_blackbox_be
- Dependencies: [[Odoo 18/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[Odoo 18/Community Addons/l10n_be/l10n_be|l10n_be]], [[Odoo 18/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]], [[Odoo 18/Community Addons/pos_hr/pos_hr|pos_hr]], [[Odoo 18/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[Odoo 18/Community Addons/pos_discount/pos_discount|pos_discount]]

## Summary

Implements the registered cash system, adhering to guidelines by FPS Finance.

## XML Artifacts (detected)

- Views: 14
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountTax`
- `HrEmployee`
- `Module`
- `pos_blackbox_be.log`
- `PosCategory`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `pos_session`
- `ProductProduct`
- `ProductTemplate`
- `ResUser`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgian Registered Cash Register - Models and Relations
class AccountTax
class HrEmployee
class Module
class "pos_blackbox_be.log" as pos_blackbox_be_log
class PosCategory
class PosConfig
class PosOrder
class PosOrderLine
class pos_session
class ProductProduct
class ProductTemplate
class ResUser
class "pos.session" as pos_session
HrEmployee .. pos_session : many2many
class "res.users" as res_users
pos_blackbox_be_log --> res_users : many2one
class "iot.device" as iot_device
PosConfig --> iot_device : many2one
pos_session .. res_users : many2many
class "hr.employee" as hr_employee
pos_session .. hr_employee : many2many
ResUser .. pos_session : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
