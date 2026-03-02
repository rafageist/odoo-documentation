<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 2, `Integer` x 4, `Selection` x 2
- Relation fields: 0

## Sample fields

- `reminder_allow`: `Boolean` (comodel `Approver Reminder`, related `company_id.timesheet_mail_allow`)
- `reminder_delay`: `Integer` (comodel `Days to Remind Approver`, related `company_id.timesheet_mail_delay`)
- `reminder_interval`: `Selection` (related `company_id.timesheet_mail_interval`)
- `reminder_user_allow`: `Boolean` (comodel `Employee Reminder`, related `company_id.timesheet_mail_employee_allow`)
- `reminder_user_delay`: `Integer` (comodel `Days to Remind User`, related `company_id.timesheet_mail_employee_delay`)
- `reminder_user_interval`: `Selection` (related `company_id.timesheet_mail_employee_interval`)
- `timesheet_min_duration`: `Integer` (comodel `Minimal Duration`)
- `timesheet_rounding`: `Integer` (comodel `Round up`)

## Method hints

- Detected methods: 0
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/timesheet_grid/Models]]

<!-- GENERATED:MODEL -->
