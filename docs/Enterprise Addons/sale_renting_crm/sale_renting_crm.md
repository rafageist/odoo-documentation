<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Opportunity to Rental

- Scope: Enterprise Addons
- Source: enterprise/sale_renting_crm
- Dependencies: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]], [[docs/Community Addons/sale_crm/sale_crm|sale_crm]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




