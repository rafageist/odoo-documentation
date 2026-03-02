<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# France - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_fr_account
- Dependencies: [[docs/Community Addons/base_iban/base_iban|base_iban]], [[docs/Community Addons/base_vat/base_vat|base_vat]], [[docs/Community Addons/account/account|account]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Community Addons/l10n_fr/l10n_fr|l10n_fr]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title France - Accounting - Models and Relations
class AccountMove
class ResCompany
class ResPartner
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





