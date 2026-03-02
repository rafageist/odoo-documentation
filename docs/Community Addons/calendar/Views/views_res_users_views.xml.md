<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Community Addons/calendar/calendar|calendar]]
- Scope: Community Addons
- Source file: `views/res_users_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_users_form_view`
- Name: res.users.form.calendar
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `calendar_default_privacy`
- XPath or positional patches: 1

### `res_users_form_view_calendar_default_privacy`
- Name: res.users.preferences.form.inherit
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `calendar_default_privacy`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/calendar/Views]]

<!-- GENERATED:VIEWFILE -->
