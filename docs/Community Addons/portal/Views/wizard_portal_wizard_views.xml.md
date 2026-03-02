<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/portal_wizard_views.xml

- Module: [[docs/Community Addons/portal/portal|portal]]
- Scope: Community Addons
- Source file: `wizard/portal_wizard_views.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `wizard_view`
- Name: Grant portal access
- Model: `portal.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `email`, `email_state`, `is_internal`, `is_portal`, `login_date`, `partner_id`, `user_ids`, `welcome_message`
- Buttons: `action_grant_access`, `action_invite_again`, `action_refresh_modal`, `action_revoke_access`
- XPath or positional patches: 0

## Actions

- `partner_wizard_action`: `act_window` Grant portal access
- `partner_wizard_action_create_and_open`: `server` Grant portal access

## Navigation

- **Parent:** [[docs/Community Addons/portal/Views]]

<!-- GENERATED:VIEWFILE -->
