<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payroll.edit.payslip.lines.wizard

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/hr_payroll_edit_payslip_lines_wizard.py`
- Python classes: `HrPayrollEditPayslipLinesWizard`
- Description: Edit payslip lines wizard

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Many2one` x 1, `One2many` x 2
- Relation fields: 3

## Sample fields

- `line_ids`: `One2many` (comodel `hr.payroll.edit.payslip.line`)
- `payslip_id`: `Many2one` (comodel `hr.payslip`)
- `worked_days_line_ids`: `One2many` (comodel `hr.payroll.edit.payslip.worked.days.line`)
- `ytd_computation`: `Boolean` (related `payslip_id.ytd_computation`)

## Method hints

- Detected methods: 4
- Action methods: `action_validate_edition`
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
title hr.payroll.edit.payslip.lines.wizard - Direct Relations
class "hr.payroll.edit.payslip.lines.wizard" as hr_payroll_edit_payslip_lines_wizard
class "hr.payroll.edit.payslip.line" as hr_payroll_edit_payslip_line
class "hr.payroll.edit.payslip.worked.days.line" as hr_payroll_edit_payslip_worked_days_line
class "hr.payslip" as hr_payslip
hr_payroll_edit_payslip_lines_wizard --> hr_payslip : payslip_id
hr_payroll_edit_payslip_lines_wizard --|> hr_payroll_edit_payslip_line : line_ids
hr_payroll_edit_payslip_lines_wizard --|> hr_payroll_edit_payslip_worked_days_line : worked_days_line_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Models]]

<!-- GENERATED:MODEL -->
