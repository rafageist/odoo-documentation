<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Account Bank Statement Extract

- Scope: Enterprise Addons
- Source: enterprise/account_bank_statement_extract
- Dependencies: [[docs/Enterprise Addons/accountant/accountant|accountant]], [[docs/Enterprise Addons/account_bank_statement_import/account_bank_statement_import|account_bank_statement_import]], [[docs/Enterprise Addons/iap_extract/iap_extract|iap_extract]], [[docs/Enterprise Addons/account_extract/account_extract|account_extract]]

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
- `AccountBankStatementLine`
- `AccountJournal`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Account Bank Statement Extract - Models and Relations
class "account.bank.statement" as account_bank_statement
class AccountBankStatementLine
class AccountJournal
class ResCompany
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



