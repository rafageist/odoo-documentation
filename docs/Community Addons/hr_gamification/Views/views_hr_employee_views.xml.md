<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Community Addons/hr_gamification/hr_gamification|hr_gamification]]
- Scope: Community Addons
- Source file: `views/hr_employee_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_public_view_form`
- Name: hr.employee.public.view.form.inherit
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_form`
- Root tag: `page`
- Field references: 2
- Sample fields: `badge_ids`, `has_badges`
- Buttons: `%(action_reward_wizard)d`
- XPath or positional patches: 1

### `hr_hr_employee_view_form`
- Name: hr.employee.view.form.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `badge_ids`, `has_badges`
- Buttons: `%(action_reward_wizard)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr_gamification/Views]]

<!-- GENERATED:VIEWFILE -->
