<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 12
- Field types: `Boolean` x 2, `Char` x 3, `Many2one` x 6, `Selection` x 1
- Relation fields: 6

## Sample fields

- `l10n_ec_edi_certificate_id`: `Many2one` (comodel `certificate.certificate`)
- `l10n_ec_forced_accounting`: `Boolean`
- `l10n_ec_legal_name`: `Char`
- `l10n_ec_production_env`: `Boolean`
- `l10n_ec_regime`: `Selection`
- `l10n_ec_special_taxpayer_number`: `Char`
- `l10n_ec_tax_base_purchase_account_id`: `Many2one` (comodel `account.account`)
- `l10n_ec_tax_base_sale_account_id`: `Many2one` (comodel `account.account`)
- `l10n_ec_withhold_agent_number`: `Char`
- `l10n_ec_withhold_credit_card_tax_id`: `Many2one` (comodel `account.tax`)
- `l10n_ec_withhold_goods_tax_id`: `Many2one` (comodel `account.tax`)
- `l10n_ec_withhold_services_tax_id`: `Many2one` (comodel `account.tax`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title res.company - Direct Relations
class "res.company" as res_company
class "account.account" as account_account
class "account.tax" as account_tax
class "certificate.certificate" as certificate_certificate
res_company --> certificate_certificate : l10n_ec_edi_certificate_id
res_company --> account_tax : l10n_ec_withhold_goods_tax_id
res_company --> account_tax : l10n_ec_withhold_services_tax_id
res_company --> account_tax : l10n_ec_withhold_credit_card_tax_id
res_company --> account_account : l10n_ec_tax_base_sale_account_id
res_company --> account_account : l10n_ec_tax_base_purchase_account_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ec_edi/Models]]

<!-- GENERATED:MODEL -->
