<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Chile - Localization: Factoring Extension

- Scope: Enterprise Addons
- Source: enterprise/l10n_cl_edi_factoring
- Dependencies: [[docs/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]]

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `Company`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Chile - Localization: Factoring Extension - Models and Relations
class AccountMove
class Company
class ResPartner
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
class "account.move" as account_move
AccountMove --|> account_move : one2many
AccountMove --> account_move : many2one
class "account.journal" as account_journal
Company --> account_journal : many2one
class "account.account" as account_account
Company --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



