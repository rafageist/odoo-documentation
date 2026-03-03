---
tags: [odoo, community, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Community Addons/microsoft_calendar/microsoft_calendar|microsoft_calendar]]
- Scope: Community Addons
- Source file: `views/res_users_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_users_form`
- Name: res.users.form
- Model: `res.users`
- Type: inferred from arch
- Inherits: `calendar.res_users_view_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `microsoft_calendar_rtoken`, `microsoft_calendar_sync_token`, `microsoft_calendar_token`, `microsoft_calendar_token_validity`, `microsoft_last_sync_date`
- Buttons: `%(microsoft_calendar_reset_account_action)d`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/microsoft_calendar/Views]]

