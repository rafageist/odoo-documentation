<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.pricelist

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/product_pricelist.py`
- Python classes: `ProductPricelist`
- Description: Pricelist
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Char` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 2, `One2many` x 1
- Relation fields: 4

## Sample fields

- `active`: `Boolean`
- `company_id`: `Many2one` (comodel `res.company`)
- `country_group_ids`: `Many2many` (comodel `res.country.group`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `item_ids`: `One2many` (comodel `product.pricelist.item`)
- `name`: `Char`
- `sequence`: `Integer`

## Method hints

- Detected methods: 21
- Action methods: `action_open_pricelist_report`
- Compute methods: `_compute_display_name`, `_compute_price_rule`, `_compute_price_rule_multi`
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
title product.pricelist - Direct Relations
class "product.pricelist" as product_pricelist
class "product.pricelist.item" as product_pricelist_item
class "res.company" as res_company
class "res.country.group" as res_country_group
class "res.currency" as res_currency
product_pricelist --> res_currency : currency_id
product_pricelist --> res_company : company_id
product_pricelist .. res_country_group : country_group_ids
product_pricelist --|> product_pricelist_item : item_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/product/Models]]

<!-- GENERATED:MODEL -->
