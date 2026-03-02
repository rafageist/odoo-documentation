<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip.run

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/l10n_hk_hr_payroll_empf|l10n_hk_hr_payroll_empf]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `model/hr_payslip_run.py`
- Python classes: `HrPayslipRun`

## Field footprint

- Detected fields: 3
- Field types: `Many2one` x 2, `One2many` x 1
- Relation fields: 3

## Sample fields

- `l10n_hk_payroll_empf_report_id`: `One2many` (comodel `l10n_hk.empf.contribution.report`)
- `l10n_hk_payroll_group_id`: `Many2one` (comodel `l10n_hk.payroll.group`)
- `l10n_hk_payroll_scheme_id`: `Many2one` (comodel `l10n_hk.mpf.scheme`)

## Method hints

- Detected methods: 4
- Action methods: `action_l10n_hk_hr_version_list_view_payrun`, `action_open_empf_contribution_report`, `action_validate`
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
title hr.payslip.run - Direct Relations
class "hr.payslip.run" as hr_payslip_run
class "l10n_hk.empf.contribution.report" as l10n_hk_empf_contribution_report
class "l10n_hk.mpf.scheme" as l10n_hk_mpf_scheme
class "l10n_hk.payroll.group" as l10n_hk_payroll_group
hr_payslip_run --> l10n_hk_mpf_scheme : l10n_hk_payroll_scheme_id
hr_payslip_run --> l10n_hk_payroll_group : l10n_hk_payroll_group_id
hr_payslip_run --|> l10n_hk_empf_contribution_report : l10n_hk_payroll_empf_report_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/Models]]

<!-- GENERATED:MODEL -->
