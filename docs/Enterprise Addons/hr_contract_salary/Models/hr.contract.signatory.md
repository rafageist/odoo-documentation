<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.contract.signatory

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_contract_signatory.py`
- Python classes: `HrContractSignatory`
- Description: Contract Signatories

## Field footprint

- Detected fields: 7
- Field types: `Integer` x 1, `Many2one` x 5, `Selection` x 1
- Relation fields: 5

## Sample fields

- `contract_template_id`: `Many2one` (comodel `hr.version`)
- `offer_id`: `Many2one` (comodel `hr.contract.salary.offer`)
- `order`: `Integer` (comodel `Sign Order`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `sign_role_id`: `Many2one` (comodel `sign.item.role`)
- `signatory`: `Selection`
- `update_contract_template_id`: `Many2one` (comodel `hr.version`)

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
title hr.contract.signatory - Direct Relations
class "hr.contract.signatory" as hr_contract_signatory
class "hr.contract.salary.offer" as hr_contract_salary_offer
class "hr.version" as hr_version
class "res.partner" as res_partner
class "sign.item.role" as sign_item_role
hr_contract_signatory --> sign_item_role : sign_role_id
hr_contract_signatory --> res_partner : partner_id
hr_contract_signatory --> hr_version : contract_template_id
hr_contract_signatory --> hr_version : update_contract_template_id
hr_contract_signatory --> hr_contract_salary_offer : offer_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Models]]

<!-- GENERATED:MODEL -->
