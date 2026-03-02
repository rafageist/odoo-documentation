<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_view.xml

- Module: [[docs/Enterprise Addons/website_helpdesk_livechat/website_helpdesk_livechat|website_helpdesk_livechat]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_view.xml`
- Views: 2
- Actions: 0
- Menus: 1
- Rules: 0

## View records

### `helpdesk_tiket_view_form_inherit_website_helpdesk_livechat`
- Name: helpdesk.ticket.view.form.inherit.website.helpdesk.livechat
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_open_livechat`
- XPath or positional patches: 1

### `helpdesk_team_view_form_inherit_website_helpdesk_livechat`
- Name: helpdesk.team.form.inherit.website.livechat.helpdesk
- Model: `helpdesk.team`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_team_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(im_livechat.chatbot_script_action)d`, `action_view_channel`
- XPath or positional patches: 1

## Menus

- `chatbot_config`: Chatbots

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_helpdesk_livechat/Views]]

<!-- GENERATED:VIEWFILE -->
