<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Opportunity to Rental

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/sale_renting_crm
- Dependencies: [[Odoo 19/Enterprise Addons/sale_renting/sale_renting|sale_renting]], [[Odoo 19/Community Addons/sale_crm/sale_crm|sale_crm]]

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `CrmLead`
- `SaleOrder`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Opportunity to Rental - Models and Relations
class CrmLead
class SaleOrder
class "sale.order" as sale_order
CrmLead --|> sale_order : one2many
class "crm.lead" as crm_lead
SaleOrder --> crm_lead : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

