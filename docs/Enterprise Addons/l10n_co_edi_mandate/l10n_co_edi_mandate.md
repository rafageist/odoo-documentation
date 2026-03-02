<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Mandate invoicing for Colombia

- Scope: Enterprise Addons
- Source: enterprise/l10n_co_edi_mandate
- Dependencies: [[docs/Enterprise Addons/l10n_co_dian/l10n_co_dian|l10n_co_dian]]

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
!include ../../../templates/DiagramStyles.puml
title Mandate invoicing for Colombia - Models and Relations
class AccountMove
class ProductTemplate
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



