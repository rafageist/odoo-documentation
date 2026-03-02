<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.salary.rule

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_salary_rule.py`
- Python classes: `HrSalaryRule`
- Description: Salary Rule

## Field footprint

- Detected fields: 39
- Field types: `Boolean` x 13, `Char` x 8, `Float` x 3, `Html` x 1, `Integer` x 1, `Many2one` x 8, `Selection` x 3, `Text` x 2
- Relation fields: 8

## Sample fields

- `active`: `Boolean`
- `amount_fix`: `Float`
- `amount_other_input_id`: `Many2one` (comodel `hr.payslip.input.type`)
- `amount_percentage`: `Float`
- `amount_percentage_base`: `Char`
- `amount_python_compute`: `Text`
- `amount_select`: `Selection`
- `appears_on_employee_cost_dashboard`: `Boolean`
- `appears_on_payslip`: `Boolean`
- `bold`: `Boolean`
- `category_id`: `Many2one` (comodel `hr.salary.rule.category`)
- `code`: `Char`
- `color`: `Char` (comodel `Color`)
- `condition_domain`: `Char`
- `condition_other_input_id`: `Many2one` (comodel `hr.payslip.input.type`)
- `condition_python`: `Text`
- `condition_select`: `Selection`
- `country_id`: `Many2one` (related `struct_id.country_id`)
- `dependent_input_id`: `Many2one` (comodel `hr.salary.rule`)
- `indented`: `Boolean`

## Method hints

- Detected methods: 9
- Action methods: none
- Compute methods: `_compute_input_used_in_definition`, `_compute_rule`
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
title hr.salary.rule - Direct Relations
class "hr.salary.rule" as hr_salary_rule
class "hr.payroll.structure" as hr_payroll_structure
class "hr.payslip.input.type" as hr_payslip_input_type
class "hr.salary.rule" as hr_salary_rule
class "hr.salary.rule.category" as hr_salary_rule_category
class "hr.salary.rule.section" as hr_salary_rule_section
class "res.partner" as res_partner
hr_salary_rule --> hr_payroll_structure : struct_id
hr_salary_rule --> hr_salary_rule_category : category_id
hr_salary_rule --> hr_payslip_input_type : condition_other_input_id
hr_salary_rule --> hr_payslip_input_type : amount_other_input_id
hr_salary_rule --> res_partner : partner_id
hr_salary_rule --> hr_salary_rule_section : input_section
hr_salary_rule --> hr_salary_rule : dependent_input_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Models]]

<!-- GENERATED:MODEL -->
