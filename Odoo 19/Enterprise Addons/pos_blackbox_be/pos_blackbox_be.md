<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Belgian Registered Cash Register

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/pos_blackbox_be
- Dependencies: [[Odoo 19/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[Odoo 19/Community Addons/l10n_be/l10n_be|l10n_be]], [[Odoo 19/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]], [[Odoo 19/Community Addons/pos_hr/pos_hr|pos_hr]], [[Odoo 19/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[Odoo 19/Community Addons/pos_discount/pos_discount|pos_discount]], [[Odoo 19/Community Addons/pos_self_order/pos_self_order|pos_self_order]], [[Odoo 19/Enterprise Addons/pos_urban_piper/pos_urban_piper|pos_urban_piper]]

## Summary

Implements the registered cash system, adhering to guidelines by FPS Finance.

## XML Artifacts (detected)

- Views: 15
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountTax`
- `HrEmployee`
- `IrModuleModule`
- `pos_blackbox_be.log`
- `pos.blackbox.log.ip`
- `PosCategory`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosSession`
- `ProductTemplate`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgian Registered Cash Register - Models and Relations
class AccountTax
class HrEmployee
class IrModuleModule
class "pos_blackbox_be.log" as pos_blackbox_be_log
class "pos.blackbox.log.ip" as pos_blackbox_log_ip
class PosCategory
class PosConfig
class PosOrder
class PosOrderLine
class PosSession
class ProductTemplate
class ResUsers
class "pos.session" as pos_session
HrEmployee .. pos_session : many2many
class "res.users" as res_users
pos_blackbox_be_log --> res_users : many2one
class "iot.device" as iot_device
PosConfig --> iot_device : many2one
PosSession .. res_users : many2many
class "hr.employee" as hr_employee
PosSession .. hr_employee : many2many
ResUsers .. pos_session : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

