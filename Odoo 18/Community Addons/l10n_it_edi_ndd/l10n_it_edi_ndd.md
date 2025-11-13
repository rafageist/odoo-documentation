<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Italy - E-invoicing - Additional module to support the debit notes (nota di debito - NDD)

- Version: v18
- Category: community
- Source: odoo/addons/l10n_it_edi_ndd
- Dependencies: [[Odoo 18/Community Addons/l10n_it_edi/l10n_it_edi|l10n_it_edi]]
## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `AccountPaymentMethodLine`
- `l10n_it.document.type`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Italy - E-invoicing - Additional module to support the debit notes (nota di debito - NDD) - Models and Relations
class AccountMove
class AccountPaymentMethodLine
class "l10n_it.document.type" as l10n_it_document_type
AccountMove --> l10n_it_document_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
