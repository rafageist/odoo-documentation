<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/gamification_challenge_views.xml

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Source file: `views/gamification_challenge_views.xml`
- Views: 4
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `challenge_search_view`
- Name: Challenge Search
- Model: `gamification.challenge`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_challenge_kanban`
- Name: Challenge Kanban
- Model: `gamification.challenge`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `line_ids`, `name`, `user_count`
- XPath or positional patches: 0

### `challenge_form_view`
- Name: Challenge Form
- Model: `gamification.challenge`
- Type: inferred from arch
- Root tag: `form`
- Field references: 28
- Sample fields: `challenge_category`, `condition`, `definition_full_suffix`, `definition_id`, `description`, `end_date`, `invited_user_ids`, `line_ids`, `manager_id`, `name`, and 18 more
- Buttons: `%(goals_from_challenge_act)d`, `action_check`, `action_report_progress`, `action_start`, `action_view_users`
- XPath or positional patches: 0

### `challenge_list_view`
- Name: Challenges List
- Model: `gamification.challenge`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `manager_id`, `name`, `period`, `state`
- XPath or positional patches: 0

## Actions

- `challenge_list_action_view2`: `view`
- `challenge_list_action_view1`: `view`
- `challenge_list_action`: `act_window` Challenges

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Views]]

<!-- GENERATED:VIEWFILE -->
