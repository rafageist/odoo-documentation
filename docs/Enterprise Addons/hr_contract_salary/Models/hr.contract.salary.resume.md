<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.contract.salary.resume

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_contract_salary_resume.py`
- Python classes: `HrContractSalaryResume`
- Description: Salary Package Resume

## Field footprint

- Detected fields: 11
- Field types: `Boolean` x 2, `Char` x 1, `Float` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 2, `Selection` x 3
- Relation fields: 3

## Sample fields

- `active`: `Boolean` (comodel `Active`)
- `benefit_ids`: `Many2many` (comodel `hr.contract.salary.benefit`)
- `category_id`: `Many2one` (comodel `hr.contract.salary.resume.category`)
- `code`: `Selection`
- `fixed_value`: `Float`
- `impacts_monthly_total`: `Boolean`
- `name`: `Char`
- `sequence`: `Integer`
- `structure_type_id`: `Many2one` (comodel `hr.payroll.structure.type`)
- `uom`: `Selection`
- `value_type`: `Selection`

## Method hints

- Detected methods: 1
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
title hr.contract.salary.resume - Direct Relations
class "hr.contract.salary.resume" as hr_contract_salary_resume
class "hr.contract.salary.benefit" as hr_contract_salary_benefit
class "hr.contract.salary.resume.category" as hr_contract_salary_resume_category
class "hr.payroll.structure.type" as hr_payroll_structure_type
hr_contract_salary_resume .. hr_contract_salary_benefit : benefit_ids
hr_contract_salary_resume --> hr_contract_salary_resume_category : category_id
hr_contract_salary_resume --> hr_payroll_structure_type : structure_type_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Models]]

<!-- GENERATED:MODEL -->
