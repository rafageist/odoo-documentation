<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/gamification_badge_views.xml

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Source file: `views/gamification_badge_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `badge_kanban_view`
- Name: Badge Kanban View
- Model: `gamification.badge`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `description`, `granted_count`, `image_1024`, `name`, `remaining_sending`, `rule_max_number`, `stat_my_monthly_sending`, `stat_this_month`, `unique_owner_ids`
- Buttons: `%(action_grant_wizard)d`
- XPath or positional patches: 0

### `badge_form_view`
- Name: Badge Form
- Model: `gamification.badge`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `active`, `challenge_ids`, `description`, `granted_count`, `granted_users_count`, `image_1920`, `level`, `name`, `remaining_sending`, `rule_auth`, and 8 more
- Buttons: `%(action_grant_wizard)d`
- XPath or positional patches: 0

### `badge_list_view`
- Name: Badge List
- Model: `gamification.badge`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `granted_count`, `name`, `rule_auth`, `stat_my`, `stat_this_month`
- XPath or positional patches: 0

### `gamification_badge_view_search`
- Name: gamification.badge.view.search
- Model: `gamification.badge`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `badge_list_action`: `act_window` Badges

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Views]]

<!-- GENERATED:VIEWFILE -->
