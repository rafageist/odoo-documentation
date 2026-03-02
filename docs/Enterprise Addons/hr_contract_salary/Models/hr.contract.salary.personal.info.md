<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.contract.salary.personal.info

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_contract_salary_personal_info.py`
- Python classes: `HrContractSalaryPersonalInfo`
- Description: Salary Package Personal Info

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 2, `Char` x 5, `Integer` x 1, `Many2one` x 4, `One2many` x 2, `Selection` x 3
- Relation fields: 6

## Sample fields

- `applies_on`: `Selection`
- `child_ids`: `One2many` (comodel `hr.contract.salary.personal.info`)
- `display_type`: `Selection`
- `dropdown_selection`: `Selection`
- `field`: `Char` (related `res_field_id.name`)
- `helper`: `Char`
- `impacts_net_salary`: `Boolean`
- `info_type_id`: `Many2one` (comodel `hr.contract.salary.personal.info.type`)
- `is_required`: `Boolean`
- `name`: `Char`
- `parent_id`: `Many2one` (comodel `hr.contract.salary.personal.info`)
- `placeholder`: `Char`
- `res_field_id`: `Many2one` (comodel `ir.model.fields`)
- `res_model`: `Char` (compute `_compute_res_model`)
- `sequence`: `Integer`
- `structure_type_id`: `Many2one` (comodel `hr.payroll.structure.type`)
- `value_ids`: `One2many` (comodel `hr.contract.salary.personal.info.value`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_res_model`
- Onchange methods: `_onchange_applies_on`

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
title hr.contract.salary.personal.info - Direct Relations
class "hr.contract.salary.personal.info" as hr_contract_salary_personal_info
class "hr.contract.salary.personal.info" as hr_contract_salary_personal_info
class "hr.contract.salary.personal.info.type" as hr_contract_salary_personal_info_type
class "hr.contract.salary.personal.info.value" as hr_contract_salary_personal_info_value
class "hr.payroll.structure.type" as hr_payroll_structure_type
class "ir.model.fields" as ir_model_fields
hr_contract_salary_personal_info --> ir_model_fields : res_field_id
hr_contract_salary_personal_info --> hr_payroll_structure_type : structure_type_id
hr_contract_salary_personal_info --> hr_contract_salary_personal_info_type : info_type_id
hr_contract_salary_personal_info --|> hr_contract_salary_personal_info_value : value_ids
hr_contract_salary_personal_info --> hr_contract_salary_personal_info : parent_id
hr_contract_salary_personal_info --|> hr_contract_salary_personal_info : child_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Models]]

<!-- GENERATED:MODEL -->
