---
tags: [odoo, community, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Community Addons/hr_presence/hr_presence|hr_presence]]
- Scope: Community Addons
- Source file: `views/hr_employee_views.xml`
- Views: 1
- Actions: 5
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_search`
- Name: hr.employee.view.search
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

## Actions

- `action_hr_employee_presence_time_off`: `server` Create a Time Off
- `action_hr_employee_presence_sms`: `server` Send a SMS
- `action_hr_employee_presence_log`: `server` Add a log note
- `action_hr_employee_presence_absent`: `server` Set Absent
- `action_hr_employee_presence_present`: `server` Set Present

## Navigation

- **Parent:** [[docs/Community Addons/hr_presence/Views]]

