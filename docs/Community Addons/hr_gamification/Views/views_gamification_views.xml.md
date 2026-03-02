<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/gamification_views.xml

- Module: [[docs/Community Addons/hr_gamification/hr_gamification|hr_gamification]]
- Scope: Community Addons
- Source file: `views/gamification_views.xml`
- Views: 2
- Actions: 4
- Menus: 4
- Rules: 0

## View records

### `view_current_badge_form`
- Name: gamification.badge.user.form
- Model: `gamification.badge.user`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `badge_id`, `comment`, `create_date`, `create_uid`
- Buttons: `unlink`
- XPath or positional patches: 0

### `hr_badge_form_view`
- Name: gamification.badge.form.inherit
- Model: `gamification.badge`
- Type: inferred from arch
- Inherits: `gamification.badge_form_view`
- Root tag: `div`
- Field references: 1
- Sample fields: `granted_employees_count`
- Buttons: `get_granted_employees`
- XPath or positional patches: 1

## Actions

- `challenge_list_action2_view2`: `view`
- `challenge_list_action2_view1`: `view`
- `challenge_list_action2`: `act_window` Challenges
- `goals_menu_groupby_action2`: `act_window` Goals History

## Menus

- `gamification_goal_menu_hr`: unnamed
- `gamification_challenge_menu_hr`: unnamed
- `gamification_badge_menu_hr`: unnamed
- `menu_hr_gamification`: Challenges

## Navigation

- **Parent:** [[docs/Community Addons/hr_gamification/Views]]

<!-- GENERATED:VIEWFILE -->
