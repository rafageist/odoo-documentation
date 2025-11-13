<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Opportunity to Quotation

- Version: v19
- Category: community
- Source: odoo19/addons/sale_crm
- Dependencies: [[Odoo 19/Community Addons/sale/sale|sale]], [[Odoo 19/Community Addons/crm/crm|crm]]
## XML Artifacts (detected)

- Views: 4
- Actions: 4
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `CrmLead`
- `CrmTeam`
- `SaleOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Opportunity to Quotation - Models and Relations
class CrmLead
class CrmTeam
class SaleOrder
class "sale.order" as sale_order
CrmLead --|> sale_order : one2many
class "crm.lead" as crm_lead
SaleOrder --> crm_lead : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
