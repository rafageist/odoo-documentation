<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Romanian SAF-T Export

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_ro_saft
- Dependencies: [[Odoo 19/Community Addons/l10n_ro/l10n_ro|l10n_ro]], [[Odoo 19/Enterprise Addons/account_saft/account_saft|account_saft]], [[Odoo 19/Enterprise Addons/account_asset/account_asset|account_asset]]

## XML Artifacts (detected)

- Views: 7
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountAsset`
- `l10n_ro_saft.account.asset.category`
- `AccountMove`
- `AccountTax`
- `l10n_ro_saft.tax.type`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Romanian SAF-T Export - Models and Relations
class AccountAsset
class "l10n_ro_saft.account.asset.category" as l10n_ro_saft_account_asset_category
class AccountMove
class AccountTax
class "l10n_ro_saft.tax.type" as l10n_ro_saft_tax_type
class ResCompany
AccountAsset --> l10n_ro_saft_account_asset_category : many2one
class "account.asset" as account_asset
l10n_ro_saft_account_asset_category --|> account_asset : one2many
AccountTax --> l10n_ro_saft_tax_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

