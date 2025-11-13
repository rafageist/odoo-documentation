<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Import/Export Invoices From XML/PDF

- Version: v18
- Category: community
- Source: odoo/addons/account_edi
- Dependencies: [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `account.edi.document`
- `account.edi.format`
- `AccountJournal`
- `AccountMove`
- `IrActionsReport`
- `IrAttachment`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Import/Export Invoices From XML/PDF - Models and Relations
class "account.edi.document" as account_edi_document
class "account.edi.format" as account_edi_format
class AccountJournal
class AccountMove
class IrActionsReport
class IrAttachment
class "account.move" as account_move
account_edi_document --> account_move : many2one
account_edi_document --> account_edi_format : many2one
class "ir.attachment" as ir_attachment
account_edi_document --> ir_attachment : many2one
AccountJournal .. account_edi_format : many2many
AccountJournal .. account_edi_format : many2many
AccountMove --|> account_edi_document : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
