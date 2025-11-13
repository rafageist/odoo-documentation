<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Documents - Import from Peppol

- Version: v19
- Category: enterprise
- Source: enterprise19/documents_account_peppol
- Dependencies: [[Odoo 19/Community Addons/account_peppol/account_peppol|account_peppol]], [[Odoo 19/Enterprise Addons/documents/documents|documents]]

## Summary

Documents from Peppol

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Account_Edi_Proxy_ClientUser`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Import from Peppol - Models and Relations
class Account_Edi_Proxy_ClientUser
class ResCompany
class "documents.document" as documents_document
ResCompany --> documents_document : many2one
class "documents.tag" as documents_tag
ResCompany .. documents_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
