<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# pos.config

- Module: [[docs/Enterprise Addons/pos_urban_piper/pos_urban_piper|pos_urban_piper]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/pos_config.py`
- Python classes: `PosConfig`

## Field footprint

- Detected fields: 8
- Field types: `Char` x 3, `Datetime` x 1, `Many2many` x 2, `Many2one` x 2
- Relation fields: 4

## Sample fields

- `name`: `Char`
- `urbanpiper_delivery_provider_ids`: `Many2many` (comodel `pos.delivery.provider`)
- `urbanpiper_fiscal_position_id`: `Many2one` (comodel `account.fiscal.position`)
- `urbanpiper_last_sync_date`: `Datetime`
- `urbanpiper_payment_methods_ids`: `Many2many` (comodel `pos.payment.method`)
- `urbanpiper_pricelist_id`: `Many2one` (comodel `product.pricelist`)
- `urbanpiper_store_identifier`: `Char`
- `urbanpiper_webhook_url`: `Char`

## Method hints

- Detected methods: 29
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
title pos.config - Direct Relations
class "pos.config" as pos_config
class "account.fiscal.position" as account_fiscal_position
class "pos.delivery.provider" as pos_delivery_provider
class "pos.payment.method" as pos_payment_method
class "product.pricelist" as product_pricelist
pos_config --> product_pricelist : urbanpiper_pricelist_id
pos_config --> account_fiscal_position : urbanpiper_fiscal_position_id
pos_config .. pos_payment_method : urbanpiper_payment_methods_ids
pos_config .. pos_delivery_provider : urbanpiper_delivery_provider_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_urban_piper/Models]]

<!-- GENERATED:MODEL -->
