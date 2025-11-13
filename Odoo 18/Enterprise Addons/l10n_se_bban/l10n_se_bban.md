<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# BBAN Plusgiro Bankgiro

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_se_bban
- Dependencies: [[Odoo 18/Enterprise Addons/account_iso20022/account_iso20022|account_iso20022]]

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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
