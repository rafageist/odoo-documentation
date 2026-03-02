<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# BBAN Plusgiro Bankgiro

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_se_bban
- Dependencies: [[Odoo 19/Enterprise Addons/account_iso20022/account_iso20022|account_iso20022]], [[Odoo 19/Community Addons/l10n_se/l10n_se|l10n_se]]

## Summary

Implements BBAN Plusgiro Bankgiro

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountBatchPayment`
- `AccountJournal`
- `ResPartnerBank`
- `se.bban.clear.range`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title BBAN Plusgiro Bankgiro - Models and Relations
class AccountBatchPayment
class AccountJournal
class ResPartnerBank
class "se.bban.clear.range" as se_bban_clear_range
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

