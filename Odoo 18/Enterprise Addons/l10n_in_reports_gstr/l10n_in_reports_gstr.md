<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Indian - GSTR India eFiling

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_in_reports_gstr
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_in_reports/l10n_in_reports|l10n_in_reports]], [[Odoo 18/Community Addons/l10n_in_edi/l10n_in_edi|l10n_in_edi]]
## XML Artifacts (detected)

- Views: 10
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountJournal`
- `AccountMove`
- `l10n_in.gst.return.period`
- `IrAttachment`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - GSTR India eFiling - Models and Relations
class AccountJournal
class AccountMove
class "l10n_in.gst.return.period" as l10n_in_gst_return_period
class IrAttachment
class ResCompany
AccountMove --> l10n_in_gst_return_period : many2one
class "account.tax.unit" as account_tax_unit
l10n_in_gst_return_period --> account_tax_unit : many2one
class "res.company" as res_company
l10n_in_gst_return_period --> res_company : many2one
class "res.currency" as res_currency
l10n_in_gst_return_period --> res_currency : many2one
class "ir.attachment" as ir_attachment
l10n_in_gst_return_period .. ir_attachment : many2many
class "account.move" as account_move
l10n_in_gst_return_period --> account_move : many2one
l10n_in_gst_return_period .. ir_attachment : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
