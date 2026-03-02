<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.leave

- Module: [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_leave.py`
- Python classes: `HrLeave`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `employee_registration_number`: `Char` (related `employee_id.registration_number`)
- `payslip_state`: `Selection`

## Method hints

- Detected methods: 15
- Action methods: `action_refuse`, `action_report_to_next_month`, `action_reset_confirm`
- Compute methods: `_compute_can_back_to_approve`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll_holidays/Models]]

<!-- GENERATED:MODEL -->
