<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# starshipit.shipping.wizard

- Module: [[docs/Enterprise Addons/delivery_starshipit/delivery_starshipit|delivery_starshipit]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/starshipit_shipping_wizard.py`
- Python classes: `StarshipitShippingWizard`
- Description: Choose from the available starshipit shipping methods

## Field footprint

- Detected fields: 3
- Field types: `Char` x 1, `Json` x 1, `Many2one` x 1
- Relation fields: 1

## Sample fields

- `available_services`: `Json`
- `carrier_id`: `Many2one` (comodel `delivery.carrier`)
- `selected_service_code`: `Char`

## Method hints

- Detected methods: 1
- Action methods: `action_validate`
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
title starshipit.shipping.wizard - Direct Relations
class "starshipit.shipping.wizard" as starshipit_shipping_wizard
class "delivery.carrier" as delivery_carrier
starshipit_shipping_wizard --> delivery_carrier : carrier_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_starshipit/Models]]

<!-- GENERATED:MODEL -->
