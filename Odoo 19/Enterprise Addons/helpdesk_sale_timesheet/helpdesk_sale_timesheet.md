<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Sell Helpdesk Timesheet

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/helpdesk_sale_timesheet
- Dependencies: [[Odoo 19/Enterprise Addons/helpdesk_timesheet/helpdesk_timesheet|helpdesk_timesheet]], [[Odoo 19/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]], [[Odoo 19/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]]

## Summary

Project, Helpdesk, Timesheet and Sale Orders

## XML Artifacts (detected)

- Views: 10
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountAnalyticLine`
- `HelpdeskSla`
- `HelpdeskTeam`
- `HelpdeskTicket`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sell Helpdesk Timesheet - Models and Relations
class AccountAnalyticLine
class HelpdeskSla
class HelpdeskTeam
class HelpdeskTicket
class SaleOrder
class SaleOrderLine
class "product.template" as product_template
HelpdeskSla .. product_template : many2many
class "sale.order" as sale_order
HelpdeskTicket --> sale_order : many2one
class "sale.order.line" as sale_order_line
HelpdeskTicket --> sale_order_line : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

