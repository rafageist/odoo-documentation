<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_activity_plan_views.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/mail_activity_plan_views.xml`
- Views: 4
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `mail_activity_plan_view_tree`
- Name: mail.activity.plan.view.list.inherit.hr
- Model: `mail.activity.plan`
- Type: inferred from arch
- Inherits: `mail.mail_activity_plan_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `department_id`
- XPath or positional patches: 1

### `mail_activity_plan_view_form_hr_employee`
- Name: mail.activity.plan.view.form.hr.employee
- Model: `mail.activity.plan`
- Type: inferred from arch
- Inherits: `mail.mail_activity_plan_view_form_fixed_model`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mail_activity_plan_view_form`
- Name: mail.activity.plan.view.form.inherit.hr
- Model: `mail.activity.plan`
- Type: inferred from arch
- Inherits: `mail.mail_activity_plan_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `department_assignable`, `department_id`, `responsible_type`
- XPath or positional patches: 2

### `mail_activity_plan_template_view_form`
- Name: mail.activity.plan.template.view.form.inherit.hr
- Model: `mail.activity.plan.template`
- Type: inferred from arch
- Inherits: `mail.mail_activity_plan_template_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `responsible_type`
- XPath or positional patches: 1

## Actions

- `plan_wizard_action`: `act_window` Launch Plan
- `mail_activity_plan_action_employee_view_form`: `view`
- `mail_activity_plan_action_employee_view_tree`: `view`
- `mail_activity_plan_action`: `act_window` Employee Plans

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
