<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Opportunity to Quotation

- Version: v18
- Category: community
- Source: odoo/addons/sale_crm
- Dependencies: [[Odoo 18/Community Addons/sale/sale|sale]], [[Odoo 18/Community Addons/crm/crm|crm]]
## XML Artifacts (detected)

- Views: 5
- Actions: 4
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `CrmLead`
- `CrmTeam`
- `ResUsers`
- `SaleOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Opportunity to Quotation - Models and Relations
class CrmLead
class CrmTeam
class ResUsers
class SaleOrder
class "sale.order" as sale_order
CrmLead --|> sale_order : one2many
class "crm.lead" as crm_lead
SaleOrder --> crm_lead : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
