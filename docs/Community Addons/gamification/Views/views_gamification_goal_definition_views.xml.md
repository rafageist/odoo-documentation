<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/gamification_goal_definition_views.xml

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Source file: `views/gamification_goal_definition_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `goal_definition_search_view`
- Name: Goal Definition Search
- Model: `gamification.goal.definition`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `field_id`, `model_id`, `name`
- XPath or positional patches: 0

### `goal_definition_form_view`
- Name: Goal Definitions Form
- Model: `gamification.goal.definition`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `action_id`, `batch_distinctive_field`, `batch_mode`, `batch_user_expression`, `computation_mode`, `compute_code`, `condition`, `description`, `display_mode`, `domain`, and 8 more
- XPath or positional patches: 0

### `goal_definition_list_view`
- Name: Goal Definitions List
- Model: `gamification.goal.definition`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `computation_mode`, `name`
- XPath or positional patches: 0

## Actions

- `goal_definition_list_action`: `act_window` Goal Definitions

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Views]]

<!-- GENERATED:VIEWFILE -->
