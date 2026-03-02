<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/gamification_badge_user_wizard_views.xml

- Module: [[docs/Community Addons/hr_gamification/hr_gamification|hr_gamification]]
- Scope: Community Addons
- Source file: `wizard/gamification_badge_user_wizard_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_badge_wizard_reward`
- Name: gamification.badge.user.wizard.form
- Model: `gamification.badge.user.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `badge_id`, `comment`, `employee_id`, `user_id`
- Buttons: `action_grant_badge`
- XPath or positional patches: 0

### `view_badge_wizard_grant_employee`
- Name: gamification.badge.user.wizard.form.inherit
- Model: `gamification.badge.user.wizard`
- Type: inferred from arch
- Inherits: `gamification.view_badge_wizard_grant`
- Root tag: `data`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 1

## Actions

- `action_reward_wizard`: `act_window` Grant a badge

## Navigation

- **Parent:** [[docs/Community Addons/hr_gamification/Views]]

<!-- GENERATED:VIEWFILE -->
