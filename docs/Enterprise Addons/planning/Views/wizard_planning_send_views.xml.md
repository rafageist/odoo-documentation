<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/planning_send_views.xml

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Source file: `wizard/planning_send_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `employee_no_email_list_wizard`
- Name: planning.send.employee.no.mail.wizard
- Model: `planning.send`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `employees_no_email`, `name`, `work_email`
- Buttons: `action_send`
- XPath or positional patches: 0

### `planning_send_view_form`
- Name: planning.send.form
- Model: `planning.send`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `employee_ids`, `end_datetime`, `include_unassigned`, `note`, `slot_ids`, `start_datetime`
- Buttons: `action_check_emails`, `discard`
- XPath or positional patches: 0

## Actions

- `planning_send_action`: `act_window` Publish & Send the Schedule by Email

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Views]]

<!-- GENERATED:VIEWFILE -->
