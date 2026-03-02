<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Opportunity to Quotation

- Scope: Community Addons
- Source: odoo/addons/sale_crm
- Dependencies: [[docs/Community Addons/sale/sale|sale]], [[docs/Community Addons/crm/crm|crm]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




