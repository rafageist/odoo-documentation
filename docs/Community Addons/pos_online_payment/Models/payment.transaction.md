<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# payment.transaction

- Module: [[docs/Community Addons/pos_online_payment/pos_online_payment|pos_online_payment]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/payment_transaction.py`
- Python classes: `PaymentTransaction`

## Field footprint

- Detected fields: 1
- Field types: `Many2one` x 1
- Relation fields: 1

## Sample fields

- `pos_order_id`: `Many2one` (comodel `pos.order`)

## Method hints

- Detected methods: 4
- Action methods: `action_view_pos_order`
- Compute methods: `_compute_reference_prefix`
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
title payment.transaction - Direct Relations
class "payment.transaction" as payment_transaction
class "pos.order" as pos_order
payment_transaction --> pos_order : pos_order_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/pos_online_payment/Models]]

<!-- GENERATED:MODEL -->
