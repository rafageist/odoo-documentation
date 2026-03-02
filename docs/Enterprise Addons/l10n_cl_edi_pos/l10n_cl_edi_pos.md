
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Chilean module for Point of Sale

- Scope: Enterprise Addons
- Source: enterprise/l10n_cl_edi_pos
- Dependencies: [[docs/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Chilean module for Point of Sale

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `account.move`
- `l10n_latam.document.type`
- `l10n_latam.identification.type`
- `PosConfig`
- `PosOrder`
- `PosPaymentMethod`
- `PosSession`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Chilean module for Point of Sale - Models and Relations
class "account.move" as account_move
class "l10n_latam.document.type" as l10n_latam_document_type
class "l10n_latam.identification.type" as l10n_latam_identification_type
class PosConfig
class PosOrder
class PosPaymentMethod
class PosSession
class ResCompany
class ResPartner
class "account.journal" as account_journal
PosConfig --> account_journal : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


