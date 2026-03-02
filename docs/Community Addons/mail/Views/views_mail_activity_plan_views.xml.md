<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_activity_plan_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_activity_plan_views.xml`
- Views: 6
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `mail_activity_plan_view_form_fixed_model`
- Name: mail.activity.plan.view.form.fixed.model
- Model: `mail.activity.plan`
- Type: inferred from arch
- Inherits: `mail.mail_activity_plan_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `mail_activity_plan_view_kanban`
- Name: mail.activity.plan.view.kanban
- Model: `mail.activity.plan`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `name`, `res_model_id`, `steps_count`
- XPath or positional patches: 0

### `mail_activity_plan_view_form`
- Name: mail.activity.plan.view.form
- Model: `mail.activity.plan`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `active`, `activity_type_id`, `company_id`, `delay_count`, `delay_from`, `delay_unit`, `icon`, `name`, `next_activity_ids`, `note`, and 6 more
- XPath or positional patches: 0

### `mail_activity_plan_view_tree_detailed`
- Name: mail.activity.plan.view.list.detailed
- Model: `mail.activity.plan`
- Type: inferred from arch
- Inherits: `mail.mail_activity_plan_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mail_activity_plan_view_tree`
- Name: mail.activity.plan.view.list
- Model: `mail.activity.plan`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `name`, `res_model_id`, `steps_count`
- XPath or positional patches: 0

### `mail_activity_plan_view_search`
- Name: mail.activity.plan.view.search
- Model: `mail.activity.plan`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `mail_activity_plan_view_form_action`: `view`
- `mail_activity_plan_view_tree_action`: `view`
- `mail_activity_plan_action`: `act_window` Activity Plans

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
