<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# CFDI 4.0 fields for sale orders

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_mx_edi_sale
- Dependencies: [[Odoo 19/Community Addons/sale/sale|sale]], [[Odoo 19/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title CFDI 4.0 fields for sale orders - Models and Relations
class SaleOrder
class SaleOrderLine
class "l10n_mx_edi.payment.method" as l10n_mx_edi_payment_method
SaleOrder --> l10n_mx_edi_payment_method : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
