---
tags: [odoo, enterprise, generated, views]
---

# views/hr_work_entry_views.xml

- Module: [[docs/Enterprise Addons/hr_work_entry_holidays_enterprise/hr_work_entry_holidays_enterprise|hr_work_entry_holidays_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/hr_work_entry_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `payroll_leave_hr_work_entry_type_view_form_inherit`
- Name: payroll.leave.hr.work.entry.type.view.form.inherit
- Model: `hr.work.entry.type`
- Type: inferred from arch
- Inherits: `hr_work_entry.hr_work_entry_type_view_form`
- Root tag: `group`
- Field references: 1
- Sample fields: `leave_type_ids`
- XPath or positional patches: 1

### `payroll_hr_work_entry_view_form_inherit_contract`
- Name: payroll.hr.work.entry.view.form.inherit.contract
- Model: `hr.work.entry`
- Type: inferred from arch
- Inherits: `hr_work_entry.hr_work_entry_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `payroll_hr_work_entry_view_form_inherit`
- Name: payroll.hr.work.entry.view.form.inherit
- Model: `hr.work.entry`
- Type: inferred from arch
- Inherits: `hr_work_entry.hr_work_entry_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `leave_id`, `leave_state`, `version_id`
- Buttons: `action_approve_leave`, `action_refuse_leave`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_work_entry_holidays_enterprise/Views]]

