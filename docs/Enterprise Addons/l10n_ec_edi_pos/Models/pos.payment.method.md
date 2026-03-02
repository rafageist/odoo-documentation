<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# pos.payment.method

- Module: [[docs/Enterprise Addons/l10n_ec_edi_pos/l10n_ec_edi_pos|l10n_ec_edi_pos]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/pos_payment_method.py`
- Python classes: `PosPaymentMethod`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Many2one` x 1
- Relation fields: 1

## Sample fields

- `country_code`: `Char` (related `company_id.country_id.code`)
- `l10n_ec_sri_payment_id`: `Many2one` (comodel `l10n_ec.sri.payment`)

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
title pos.payment.method - Direct Relations
class "pos.payment.method" as pos_payment_method
class "l10n_ec.sri.payment" as l10n_ec_sri_payment
pos_payment_method --> l10n_ec_sri_payment : l10n_ec_sri_payment_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ec_edi_pos/Models]]

<!-- GENERATED:MODEL -->
