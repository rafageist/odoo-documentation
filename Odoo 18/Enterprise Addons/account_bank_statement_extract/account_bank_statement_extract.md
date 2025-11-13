<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Account Bank Statement Extract

- Version: v18
- Category: enterprise
- Source: enterprise18/account_bank_statement_extract
- Dependencies: [[Odoo 18/Enterprise Addons/accountant/accountant|accountant]], [[Odoo 18/Enterprise Addons/account_bank_statement_import/account_bank_statement_import|account_bank_statement_import]], [[Odoo 18/Enterprise Addons/iap_extract/iap_extract|iap_extract]], [[Odoo 18/Enterprise Addons/account_extract/account_extract|account_extract]]

## Summary

Extract data from bank statement scans to fill them automatically

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `account.bank.statement`
- `AccountJournal`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Account Bank Statement Extract - Models and Relations
class "account.bank.statement" as account_bank_statement
class AccountJournal
class ResCompany
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
