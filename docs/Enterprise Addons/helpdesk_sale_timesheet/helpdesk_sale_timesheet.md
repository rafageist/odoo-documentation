<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sell Helpdesk Timesheet

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_sale_timesheet
- Dependencies: [[docs/Enterprise Addons/helpdesk_timesheet/helpdesk_timesheet|helpdesk_timesheet]], [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]], [[docs/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




