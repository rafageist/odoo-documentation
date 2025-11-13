<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Accounting Reports

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_reports
- Dependencies: [[Odoo 18/Community Addons/l10n_be/l10n_be|l10n_be]], [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]], [[Odoo 18/Enterprise Addons/account_loans/account_loans|account_loans]]
## XML Artifacts (detected)

- Views: 12
- Actions: 13
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 6

## Detected Models

- `l10n_be.form.281.50`
- `l10n_be.form.325`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Accounting Reports - Models and Relations
class "l10n_be.form.281.50" as l10n_be_form_281_50
class "l10n_be.form.325" as l10n_be_form_325
class ResCompany
class ResPartner
l10n_be_form_281_50 --> l10n_be_form_325 : many2one
class "res.company" as res_company
l10n_be_form_281_50 --> res_company : many2one
class "res.partner" as res_partner
l10n_be_form_281_50 --> res_partner : many2one
class "res.country" as res_country
l10n_be_form_281_50 --> res_country : many2one
class "res.currency" as res_currency
l10n_be_form_281_50 --> res_currency : many2one
l10n_be_form_325 --> res_company : many2one
class "res.users" as res_users
l10n_be_form_325 --> res_users : many2one
l10n_be_form_325 --> res_partner : many2one
l10n_be_form_325 --> res_partner : many2one
l10n_be_form_325 --> res_country : many2one
l10n_be_form_325 --> res_currency : many2one
l10n_be_form_325 --|> l10n_be_form_281_50 : one2many
ResPartner --|> l10n_be_form_281_50 : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
