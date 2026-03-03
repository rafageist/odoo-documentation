---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_views.xml

- Module: [[docs/Enterprise Addons/website_helpdesk_forum/website_helpdesk_forum|website_helpdesk_forum]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_team_view_form_inherit_website_helpdesk_forum`
- Name: helpdesk.team.form.inherit.website.forum
- Model: `helpdesk.team`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_team_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `website_forum_ids`
- XPath or positional patches: 1

### `helpdesk_ticket_view_form_inherit_website_helpdesk_forum`
- Name: Tickets: Website
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `can_share_forum`, `forum_post_count`, `use_website_helpdesk_forum`
- Buttons: `action_open_forum_posts`, `action_share_ticket_on_forum`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_helpdesk_forum/Views]]

