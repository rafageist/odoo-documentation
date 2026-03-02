<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Netherlands - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_nl
- Dependencies: [[docs/Community Addons/base_iban/base_iban|base_iban]], [[docs/Community Addons/base_vat/base_vat|base_vat]], [[docs/Community Addons/account/account|account]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountJournal`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Netherlands - Accounting - Models and Relations
class AccountJournal
class ResCompany
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





