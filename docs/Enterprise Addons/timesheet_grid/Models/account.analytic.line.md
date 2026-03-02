<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.analytic.line

- Module: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/account_analytic_line.py`
- Python classes: `AccountAnalyticLine`
- Inherits: `timer.mixin`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 4, `Monetary` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `amount`: `Monetary`
- `display_timer`: `Boolean` (comodel `Technical field used to display the timer if the encoding unit is 'Hours'.`, compute `_compute_display_timer`)
- `is_hatched`: `Boolean` (compute `_compute_is_hatched`)
- `user_can_validate`: `Boolean` (compute `_compute_can_validate`)
- `validated`: `Boolean` (comodel `Validated line`, store `True`)
- `validated_status`: `Selection` (compute `_compute_validated_status`)

## Method hints

- Detected methods: 50
- Action methods: `action_add_time_to_timer`, `action_add_time_to_timesheet`, `action_change_project_task`, `action_invalidate_timesheet`, `action_merge_timesheets`, `action_start_new_timesheet_timer`, `action_timer_decrease`, `action_timer_increase`, and 4 more
- Compute methods: `_compute_can_validate`, `_compute_display_timer`, `_compute_is_hatched`, `_compute_project_id`, `_compute_validated_status`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/timesheet_grid/Models]]

<!-- GENERATED:MODEL -->
