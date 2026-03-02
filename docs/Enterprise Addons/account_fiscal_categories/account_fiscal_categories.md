<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Account Fiscal Report

- Scope: Enterprise Addons
- Source: enterprise/account_fiscal_categories
- Dependencies: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## Summary

Account Fiscal Report

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `AccountAccount`
- `account.account.fiscal.rate`
- `account.fiscal.category`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Account Fiscal Report - Models and Relations
class AccountAccount
class "account.account.fiscal.rate" as account_account_fiscal_rate
class "account.fiscal.category" as account_fiscal_category
AccountAccount --> account_fiscal_category : many2one
AccountAccount --|> account_account_fiscal_rate : one2many
class "account.account" as account_account
account_account_fiscal_rate --> account_account : many2one
class "res.company" as res_company
account_account_fiscal_rate --> res_company : many2one
account_fiscal_category --> res_company : many2one
account_fiscal_category --|> account_account : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



