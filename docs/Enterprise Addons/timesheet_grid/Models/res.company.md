<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 2, `Datetime` x 2, `Integer` x 2, `Selection` x 2
- Relation fields: 0

## Sample fields

- `timesheet_mail_allow`: `Boolean` (comodel `Approver Reminder`)
- `timesheet_mail_delay`: `Integer` (comodel `Approver Reminder Days`)
- `timesheet_mail_employee_allow`: `Boolean` (comodel `Employee Reminder`)
- `timesheet_mail_employee_delay`: `Integer` (comodel `Employee Reminder Days`)
- `timesheet_mail_employee_interval`: `Selection`
- `timesheet_mail_employee_nextdate`: `Datetime` (comodel `Next scheduled date for employee reminder`)
- `timesheet_mail_interval`: `Selection`
- `timesheet_mail_nextdate`: `Datetime` (comodel `Next scheduled date for approver reminder`)

## Method hints

- Detected methods: 11
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/timesheet_grid/Models]]

<!-- GENERATED:MODEL -->
