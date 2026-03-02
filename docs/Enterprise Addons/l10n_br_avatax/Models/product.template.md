<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# product.template

- Module: [[docs/Enterprise Addons/l10n_br_avatax/l10n_br_avatax|l10n_br_avatax]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/product_template.py`
- Python classes: `ProductTemplate`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 1, `Char` x 1, `Many2many` x 1, `Many2one` x 3, `Selection` x 4
- Relation fields: 4

## Sample fields

- `l10n_br_cest_code`: `Char`
- `l10n_br_company_city_id`: `Many2one` (comodel `res.city`, compute `_compute_l10n_br_company_city_id`)
- `l10n_br_labor`: `Boolean` (comodel `Labor Assignment`)
- `l10n_br_ncm_code_id`: `Many2one` (comodel `l10n_br.ncm.code`)
- `l10n_br_property_service_code_origin_id`: `Many2one` (comodel `l10n_br.service.code`)
- `l10n_br_service_code_ids`: `Many2many` (comodel `l10n_br.service.code`)
- `l10n_br_source_origin`: `Selection`
- `l10n_br_sped_type`: `Selection`
- `l10n_br_transport_cost_type`: `Selection`
- `l10n_br_use_type`: `Selection`

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_l10n_br_company_city_id`
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
title product.template - Direct Relations
class "product.template" as product_template
class "l10n_br.ncm.code" as l10n_br_ncm_code
class "l10n_br.service.code" as l10n_br_service_code
class "res.city" as res_city
product_template --> l10n_br_ncm_code : l10n_br_ncm_code_id
product_template --> l10n_br_service_code : l10n_br_property_service_code_origin_id
product_template .. l10n_br_service_code : l10n_br_service_code_ids
product_template --> res_city : l10n_br_company_city_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_br_avatax/Models]]

<!-- GENERATED:MODEL -->
