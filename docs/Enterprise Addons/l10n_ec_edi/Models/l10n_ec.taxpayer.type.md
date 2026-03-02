<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_ec.taxpayer.type

- Module: [[docs/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/l10n_ec_taxpayer_type.py`
- Python classes: `L10n_EcTaxpayerType`
- Description: Taxpayer Type

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 1, `Integer` x 1, `Many2one` x 3
- Relation fields: 3

## Sample fields

- `active`: `Boolean`
- `name`: `Char`
- `profit_withhold_tax_id`: `Many2one` (comodel `account.tax`)
- `sequence`: `Integer`
- `vat_goods_withhold_tax_id`: `Many2one` (comodel `account.tax`)
- `vat_services_withhold_tax_id`: `Many2one` (comodel `account.tax`)

## Method hints

- Detected methods: 0
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
title l10n_ec.taxpayer.type - Direct Relations
class "l10n_ec.taxpayer.type" as l10n_ec_taxpayer_type
class "account.tax" as account_tax
l10n_ec_taxpayer_type --> account_tax : profit_withhold_tax_id
l10n_ec_taxpayer_type --> account_tax : vat_goods_withhold_tax_id
l10n_ec_taxpayer_type --> account_tax : vat_services_withhold_tax_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ec_edi/Models]]

<!-- GENERATED:MODEL -->
