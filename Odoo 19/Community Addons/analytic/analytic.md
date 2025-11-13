<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Analytic Accounting

- Version: v19
- Category: community
- Source: odoo19/addons/analytic
- Dependencies: base (not documented), [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/uom/uom|uom]]
## XML Artifacts (detected)

- Views: 15
- Actions: 6
- Menus: 0
- Rules (ir.rule): 4
- Access CSV entries: 5

## Detected Models

- `account.analytic.account`
- `account.analytic.distribution.model`
- `account.analytic.line`
- `account.analytic.plan`
- `account.analytic.applicability`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Analytic Accounting - Models and Relations
class "account.analytic.account" as account_analytic_account
class "account.analytic.distribution.model" as account_analytic_distribution_model
class "account.analytic.line" as account_analytic_line
class "account.analytic.plan" as account_analytic_plan
class "account.analytic.applicability" as account_analytic_applicability
account_analytic_account --> account_analytic_plan : many2one
account_analytic_account --> account_analytic_plan : many2one
account_analytic_account --|> account_analytic_line : one2many
class "res.company" as res_company
account_analytic_account --> res_company : many2one
class "res.partner" as res_partner
account_analytic_account --> res_partner : many2one
account_analytic_distribution_model --> res_partner : many2one
class "res.partner.category" as res_partner_category
account_analytic_distribution_model --> res_partner_category : many2one
account_analytic_distribution_model --> res_company : many2one
class "uom.uom" as uom_uom
account_analytic_line --> uom_uom : many2one
account_analytic_line --> res_partner : many2one
class "res.users" as res_users
account_analytic_line --> res_users : many2one
account_analytic_line --> res_company : many2one
account_analytic_plan --> account_analytic_plan : many2one
account_analytic_plan --> account_analytic_plan : many2one
account_analytic_plan --|> account_analytic_plan : one2many
account_analytic_plan --|> account_analytic_account : one2many
account_analytic_plan --|> account_analytic_applicability : one2many
account_analytic_applicability --> account_analytic_plan : many2one
account_analytic_applicability --> res_company : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
