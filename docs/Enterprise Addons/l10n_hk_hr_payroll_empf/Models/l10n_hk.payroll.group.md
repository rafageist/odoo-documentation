<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_hk.payroll.group

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/l10n_hk_hr_payroll_empf|l10n_hk_hr_payroll_empf]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `model/payroll_group.py`
- Python classes: `l10n_hkPayrollGroup`
- Description: Hong Kong: Payroll Group

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Char` x 2, `Many2one` x 2, `One2many` x 1, `Selection` x 1
- Relation fields: 3

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `contribution_frequency`: `Selection`
- `employee_ids`: `One2many` (comodel `hr.employee`)
- `group_id`: `Char`
- `is_default`: `Boolean`
- `name`: `Char`
- `scheme_id`: `Many2one` (comodel `l10n_hk.mpf.scheme`)

## Method hints

- Detected methods: 3
- Action methods: `action_open_employee_list`
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
title l10n_hk.payroll.group - Direct Relations
class "l10n_hk.payroll.group" as l10n_hk_payroll_group
class "hr.employee" as hr_employee
class "l10n_hk.mpf.scheme" as l10n_hk_mpf_scheme
class "res.company" as res_company
l10n_hk_payroll_group --> res_company : company_id
l10n_hk_payroll_group --> l10n_hk_mpf_scheme : scheme_id
l10n_hk_payroll_group --|> hr_employee : employee_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/Models]]

<!-- GENERATED:MODEL -->
