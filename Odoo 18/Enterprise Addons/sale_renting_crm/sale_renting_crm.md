<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Opportunity to Rental

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_renting_crm
- Dependencies: [[Odoo 18/Enterprise Addons/sale_renting/sale_renting|sale_renting]], [[Odoo 18/Community Addons/sale_crm/sale_crm|sale_crm]]
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
