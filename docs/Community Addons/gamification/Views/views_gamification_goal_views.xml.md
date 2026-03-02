<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/gamification_goal_views.xml

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Source file: `views/gamification_goal_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `goal_kanban_view`
- Name: Goal Kanban View
- Model: `gamification.goal`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 12
- Sample fields: `color`, `current`, `definition_condition`, `definition_display`, `definition_id`, `definition_suffix`, `end_date`, `last_update`, `start_date`, `state`, and 2 more
- XPath or positional patches: 0

### `goal_search_view`
- Name: Goal Search
- Model: `gamification.goal`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `challenge_id`, `definition_id`, `user_id`
- XPath or positional patches: 0

### `goal_form_view`
- Name: Goal Form
- Model: `gamification.goal`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `challenge_id`, `computation_mode`, `current`, `definition_condition`, `definition_id`, `definition_suffix`, `end_date`, `last_update`, `remind_update_delay`, `start_date`, and 3 more
- Buttons: `action_cancel`, `action_fail`, `action_reach`, `action_start`, `update_goal`
- XPath or positional patches: 0

### `goal_list_view`
- Name: Goal List
- Model: `gamification.goal`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `completeness`, `current`, `definition_id`, `end_date`, `line_id`, `start_date`, `state`, `target_goal`, `user_id`
- XPath or positional patches: 0

## Actions

- `goals_from_challenge_act`: `act_window` Related Goals
- `goal_list_action`: `act_window` Goals

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Views]]

<!-- GENERATED:VIEWFILE -->
