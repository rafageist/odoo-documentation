<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Account Invoice Extract

- Version: v18
- Category: enterprise
- Source: enterprise18/account_invoice_extract
- Dependencies: [[Odoo 18/Enterprise Addons/account_extract/account_extract|account_extract]]

## Summary

Extract data from invoice scans to fill them automatically

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `account.invoice_extract.words`
- `account.move`
- `IrAttachment`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Account Invoice Extract - Models and Relations
class "account.invoice_extract.words" as account_invoice_extract_words
class "account.move" as account_move
class IrAttachment
class ResCompany
account_invoice_extract_words --> account_move : many2one
account_move --|> account_invoice_extract_words : one2many
class "ir.attachment" as ir_attachment
account_move --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
