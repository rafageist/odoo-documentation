<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Italy - Declaration of Intent

- Scope: Community Addons
- Source: odoo/addons/l10n_it_edi_doi
- Dependencies: [[docs/Community Addons/l10n_it_edi/l10n_it_edi|l10n_it_edi]], [[docs/Community Addons/sale/sale|sale]]

## XML Artifacts (detected)

- Views: 11
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountFiscalPosition`
- `AccountMove`
- `AccountTax`
- `l10n_it_edi_doi.declaration_of_intent`
- `ResCompany`
- `ResPartner`
- `SaleOrder`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Italy - Declaration of Intent - Models and Relations
class AccountFiscalPosition
class AccountMove
class AccountTax
class "l10n_it_edi_doi.declaration_of_intent" as l10n_it_edi_doi_declaration_of_intent
class ResCompany
class ResPartner
class SaleOrder
AccountMove --> l10n_it_edi_doi_declaration_of_intent : many2one
class "res.company" as res_company
l10n_it_edi_doi_declaration_of_intent --> res_company : many2one
class "res.partner" as res_partner
l10n_it_edi_doi_declaration_of_intent --> res_partner : many2one
class "res.currency" as res_currency
l10n_it_edi_doi_declaration_of_intent --> res_currency : many2one
class "account.move" as account_move
l10n_it_edi_doi_declaration_of_intent --|> account_move : one2many
class "sale.order" as sale_order
l10n_it_edi_doi_declaration_of_intent --|> sale_order : one2many
class "account.tax" as account_tax
ResCompany --> account_tax : many2one
class "account.fiscal.position" as account_fiscal_position
ResCompany --> account_fiscal_position : many2one
ResPartner --|> l10n_it_edi_doi_declaration_of_intent : one2many
SaleOrder --> l10n_it_edi_doi_declaration_of_intent : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





