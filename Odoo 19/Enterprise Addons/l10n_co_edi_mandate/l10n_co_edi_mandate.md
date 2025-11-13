<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Mandate invoicing for Colombia

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_co_edi_mandate
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_co_dian/l10n_co_dian|l10n_co_dian]]

## Summary

Colombian EDI Mandate Invoicing extension

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `ProductTemplate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mandate invoicing for Colombia - Models and Relations
class AccountMove
class ProductTemplate
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
