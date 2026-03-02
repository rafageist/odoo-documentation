<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sign.item

- Module: [[docs/Enterprise Addons/sign/sign|sign]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/sign_item.py`
- Python classes: `SignItem`
- Description: Fields to be sign on Document

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 2, `Char` x 2, `Float` x 4, `Integer` x 3, `Many2many` x 1, `Many2one` x 5
- Relation fields: 6

## Sample fields

- `alignment`: `Char`
- `constant`: `Boolean`
- `document_id`: `Many2one` (comodel `sign.document`)
- `height`: `Float`
- `name`: `Char`
- `num_options`: `Integer` (related `radio_set_id.num_options`)
- `option_ids`: `Many2many` (comodel `sign.item.option`)
- `page`: `Integer`
- `posX`: `Float`
- `posY`: `Float`
- `radio_set_id`: `Many2one` (comodel `sign.item.radio.set`)
- `required`: `Boolean`
- `responsible_id`: `Many2one` (comodel `sign.item.role`)
- `template_id`: `Many2one` (comodel `sign.template`, related `document_id.template_id`)
- `transaction_id`: `Integer`
- `type_id`: `Many2one` (comodel `sign.item.type`)
- `width`: `Float`

## Method hints

- Detected methods: 5
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
title sign.item - Direct Relations
class "sign.item" as sign_item
class "sign.document" as sign_document
class "sign.item.option" as sign_item_option
class "sign.item.radio.set" as sign_item_radio_set
class "sign.item.role" as sign_item_role
class "sign.item.type" as sign_item_type
class "sign.template" as sign_template
sign_item --> sign_document : document_id
sign_item --> sign_template : template_id
sign_item --> sign_item_type : type_id
sign_item --> sign_item_role : responsible_id
sign_item .. sign_item_option : option_ids
sign_item --> sign_item_radio_set : radio_set_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sign/Models]]

<!-- GENERATED:MODEL -->
