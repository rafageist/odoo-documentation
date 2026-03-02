<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Assets Management

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/account_asset
- Dependencies: [[Odoo 19/Enterprise Addons/accountant/accountant|accountant]]

## XML Artifacts (detected)

- Views: 14
- Actions: 7
- Menus: 4
- Rules (ir.rule): 2
- Access CSV entries: 6

## Detected Models

- `AccountAccount`
- `account.asset`
- `AccountReport`
- `account.asset.group`
- `AccountMove`
- `AccountMoveLine`
- `AccountReturn`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Assets Management - Models and Relations
class AccountAccount
class "account.asset" as account_asset
class AccountReport
class "account.asset.group" as account_asset_group
class AccountMove
class AccountMoveLine
class AccountReturn
class ResCompany
AccountAccount .. account_asset : many2many
class "res.company" as res_company
account_asset --> res_company : many2one
class "res.currency" as res_currency
account_asset --> res_currency : many2one
class "account.account" as account_account
account_asset --> account_account : many2one
account_asset --> account_asset_group : many2one
account_asset --> account_account : many2one
account_asset --> account_account : many2one
class "account.journal" as account_journal
account_asset --> account_journal : many2one
class "account.move" as account_move
account_asset --|> account_move : one2many
class "account.move.line" as account_move_line
account_asset .. account_move_line : many2many
account_asset --> account_asset : many2one
account_asset --> account_asset : many2one
account_asset --|> account_asset : one2many
account_asset --|> account_asset : one2many
account_asset_group --> res_company : many2one
account_asset_group --|> account_asset : one2many
AccountMove --> account_asset : many2one
AccountMove --|> account_asset : one2many
AccountMoveLine .. account_asset : many2many
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

## Curated analysis

### Functional role
- `account_asset` adds the fixed-asset lifecycle on top of accounting: asset recognition, depreciation schedules, revaluation, disposal, and audit-oriented reporting.
- Asset groups and report handlers make the module operationally closer to a finance control surface than to a simple master-data addon.

### Operational footprint
- `account_asset.py` contains the main depreciation logic, while `account_move.py` bridges posted entries and asset creation.
- The module also ships a dedicated report handler, an asset modification wizard, and a template download controller for bulk asset loading.

### Evidence
- Source files: `enterprise19/account_asset/models/account_asset.py`, `enterprise19/account_asset/models/account_move.py`, `enterprise19/account_asset/models/account_assets_report.py`
- UI and automation: `enterprise19/account_asset/views/account_asset_views.xml`, `enterprise19/account_asset/views/account_asset_group_views.xml`, `enterprise19/account_asset/wizard/asset_modify.py`
- Security and tests: `enterprise19/account_asset/security/account_asset_security.xml`, `enterprise19/account_asset/tests/test_account_asset.py`, `enterprise19/account_asset/tests/test_reevaluation_asset.py`

### Related notes
- `[[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]]`
- `[[Odoo 19/Core/Master Data/res_company]]`

### Rollout and migration concerns
- Activating this module on a live database requires validated company accounts, journals, and depreciation policies before importing or generating any asset entries.
- Reevaluation and disposal flows create accounting side effects that finance teams usually expect to review in both journals and reports, so cutover plans need reconciliation checkpoints.
- Odoo 18 comparison backlog was retired on 2026-03-02; keep this note focused on Odoo 19 behavior.

