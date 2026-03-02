<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Belgium - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_be_reports
- Dependencies: [[docs/Community Addons/l10n_be/l10n_be|l10n_be]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## XML Artifacts (detected)

- Views: 22
- Actions: 13
- Menus: 4
- Rules (ir.rule): 2
- Access CSV entries: 15

## Detected Models

- `l10n_be.form.281.50`
- `l10n_be.form.325`
- `AccountReturnType`
- `AccountReturn`
- `l10n_be.company.region`
- `l10n_be.company.type`
- `MailActivityType`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Belgium - Accounting Reports - Models and Relations
class "l10n_be.form.281.50" as l10n_be_form_281_50
class "l10n_be.form.325" as l10n_be_form_325
class AccountReturnType
class AccountReturn
class "l10n_be.company.region" as l10n_be_company_region
class "l10n_be.company.type" as l10n_be_company_type
class MailActivityType
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
ResCompany --> l10n_be_company_region : many2one
ResCompany --> l10n_be_company_type : many2one
ResPartner --|> l10n_be_form_281_50 : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



