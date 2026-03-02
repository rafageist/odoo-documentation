<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# approval.category

- Module: [[docs/Enterprise Addons/approvals/approvals|approvals]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/approval_category.py`
- Python classes: `ApprovalCategory`
- Description: Approval Category

## Field footprint

- Detected fields: 29
- Field types: `Binary` x 1, `Boolean` x 4, `Char` x 4, `Integer` x 3, `Many2many` x 1, `Many2one` x 2, `One2many` x 1, `PropertiesDefinition` x 1, `Selection` x 12
- Relation fields: 4

## Sample fields

- `active`: `Boolean`
- `approval_minimum`: `Integer`
- `approval_properties_definition`: `PropertiesDefinition` (comodel `Approval Properties`)
- `approval_type`: `Selection`
- `approver_ids`: `One2many` (comodel `approval.category.approver`)
- `approver_sequence`: `Boolean` (comodel `Approvers Sequence?`)
- `automated_sequence`: `Boolean` (comodel `Automated Sequence?`)
- `company_id`: `Many2one` (comodel `res.company`)
- `description`: `Char`
- `has_amount`: `Selection`
- `has_date`: `Selection`
- `has_location`: `Selection`
- `has_partner`: `Selection`
- `has_payment_method`: `Selection`
- `has_period`: `Selection`
- `has_product`: `Selection`
- `has_quantity`: `Selection`
- `has_reference`: `Selection`
- `image`: `Binary`
- `invalid_minimum`: `Boolean` (compute `_compute_invalid_minimum`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_invalid_minimum`, `_compute_request_to_validate_count`, `_compute_user_ids`
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
title approval.category - Direct Relations
class "approval.category" as approval_category
class "approval.category.approver" as approval_category_approver
class "ir.sequence" as ir_sequence
class "res.company" as res_company
class "res.users" as res_users
approval_category --> res_company : company_id
approval_category .. res_users : user_ids
approval_category --|> approval_category_approver : approver_ids
approval_category --> ir_sequence : sequence_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/approvals/Models]]

<!-- GENERATED:MODEL -->
