<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_be.274_xx.line

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/l10n_be_274_XX.py`
- Python classes: `L10n_Be274_XxLine`
- Description: 274.XX Sheets Line

## Field footprint

- Detected fields: 7
- Field types: `Many2one` x 4, `Monetary` x 2, `Selection` x 1
- Relation fields: 4

## Sample fields

- `amount`: `Monetary`
- `certificate`: `Selection` (related `employee_id.certificate`)
- `company_id`: `Many2one` (comodel `res.company`, related `sheet_id.company_id`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `company_id.currency_id`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `sheet_id`: `Many2one` (comodel `l10n_be.274_xx`)
- `taxable_amount`: `Monetary`

## Method hints

- Detected methods: 0
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
title l10n_be.274_xx.line - Direct Relations
class "l10n_be.274_xx.line" as l10n_be_274_xx_line
class "hr.employee" as hr_employee
class "l10n_be.274_xx" as l10n_be_274_xx
class "res.company" as res_company
class "res.currency" as res_currency
l10n_be_274_xx_line --> l10n_be_274_xx : sheet_id
l10n_be_274_xx_line --> hr_employee : employee_id
l10n_be_274_xx_line --> res_company : company_id
l10n_be_274_xx_line --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
