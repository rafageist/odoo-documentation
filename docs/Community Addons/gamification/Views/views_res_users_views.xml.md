<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Source file: `views/res_users_views.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `res_users_view_form`
- Name: res.users.view.form.inherit.gamification
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `karma`
- Buttons: `action_karma_report`
- XPath or positional patches: 1

## Actions

- `action_new_simplified_res_users`: `act_window` Create User
- `action_current_rank_users`: `act_window` Users

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Views]]

<!-- GENERATED:VIEWFILE -->
