<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Sell Helpdesk Timesheet

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_sale_timesheet
- Dependencies: [[Odoo 18/Enterprise Addons/helpdesk_timesheet/helpdesk_timesheet|helpdesk_timesheet]], [[Odoo 18/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]], [[Odoo 18/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]]

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
- `HelpdeskSLA`
- `HelpdeskTeam`
- `HelpdeskTicket`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sell Helpdesk Timesheet - Models and Relations
class AccountAnalyticLine
class HelpdeskSLA
class HelpdeskTeam
class HelpdeskTicket
class SaleOrder
class SaleOrderLine
class "product.template" as product_template
HelpdeskSLA .. product_template : many2many
class "sale.order" as sale_order
HelpdeskTicket --> sale_order : many2one
class "sale.order.line" as sale_order_line
HelpdeskTicket --> sale_order_line : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
