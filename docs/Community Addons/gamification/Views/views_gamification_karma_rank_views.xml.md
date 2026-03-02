<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/gamification_karma_rank_views.xml

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Source file: `views/gamification_karma_rank_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `gamification_karma_rank_view_form`
- Name: gamification.karma.rank.view.form
- Model: `gamification.karma.rank`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `create_date`, `description`, `description_motivational`, `image_1920`, `karma_min`, `name`, `rank_users_count`
- Buttons: `%(action_current_rank_users)d`
- XPath or positional patches: 0

### `gamification_karma_ranks_view_tree`
- Name: gamification.karma.ranks.view.list
- Model: `gamification.karma.rank`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `karma_min`, `name`, `rank_users_count`
- XPath or positional patches: 0

### `gamification_karma_ranks_view_search`
- Name: gamification.karma.ranks.view.search
- Model: `gamification.karma.rank`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `description`, `karma_min`, `name`, `user_ids`
- XPath or positional patches: 0

## Actions

- `gamification_karma_ranks_action`: `act_window` Ranks

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Views]]

<!-- GENERATED:VIEWFILE -->
