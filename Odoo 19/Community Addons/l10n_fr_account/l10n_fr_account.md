<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# France - Accounting

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_fr_account
- Dependencies: [[Odoo 19/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 19/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 19/Community Addons/l10n_fr/l10n_fr|l10n_fr]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


