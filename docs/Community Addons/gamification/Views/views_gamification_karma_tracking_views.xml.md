<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/gamification_karma_tracking_views.xml

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Source file: `views/gamification_karma_tracking_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `gamification_karma_tracking_view_form`
- Name: gamification.karma.tracking.view.form
- Model: `gamification.karma.tracking`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `consolidated`, `gain`, `new_value`, `old_value`, `origin_ref`, `reason`, `tracking_date`, `user_id`
- XPath or positional patches: 0

### `gamification_karma_tracking_view_tree`
- Name: gamification.karma.tracking.view.list
- Model: `gamification.karma.tracking`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `gain`, `new_value`, `old_value`, `origin_ref`, `reason`, `tracking_date`, `user_id`
- XPath or positional patches: 0

### `gamification_karma_tracking_view_search`
- Name: gamification.karma.tracking.view.search
- Model: `gamification.karma.tracking`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `origin_ref_model_name`, `tracking_date`, `user_id`
- XPath or positional patches: 0

## Actions

- `gamification_karma_tracking_action`: `act_window` Karma Tracking

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Views]]

<!-- GENERATED:VIEWFILE -->
