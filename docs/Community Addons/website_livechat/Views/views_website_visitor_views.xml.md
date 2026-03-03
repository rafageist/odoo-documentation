---
tags: [odoo, community, generated, views]
---

# views/website_visitor_views.xml

- Module: [[docs/Community Addons/website_livechat/website_livechat|website_livechat]]
- Scope: Community Addons
- Source file: `views/website_visitor_views.xml`
- Views: 4
- Actions: 4
- Menus: 1
- Rules: 0

## View records

### `website_visitor_view_search`
- Name: website.visitor.view.search.website.livechat
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `website_visitor_view_tree`
- Name: website.visitor.view.list.inherit.website.livechat
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `livechat_operator_id`
- Buttons: `action_send_chat_request`
- XPath or positional patches: 1

### `website_visitor_view_form`
- Name: website.visitor.view.form.inherit.website.livechat
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `livechat_operator_id`, `session_count`
- Buttons: `%(website_visitor_livechat_session_action)d`, `action_send_chat_request`
- XPath or positional patches: 3

### `website_visitor_view_kanban`
- Name: website.visitor.view.kanban.inherit.website.livechat
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_kanban`
- Root tag: `field`
- Field references: 4
- Sample fields: `country_id`, `livechat_operator_id`, `livechat_operator_name`, `session_count`
- Buttons: `action_send_chat_request`
- XPath or positional patches: 2

## Actions

- `website_livechat_send_chat_request_action_server`: `server` Send Chat Requests
- `website_visitor_livechat_session_action_form`: `view`
- `website_visitor_livechat_session_action_tree`: `view`
- `website_visitor_livechat_session_action`: `act_window` Visitor's Sessions

## Menus

- `website_livechat_visitor_menu`: Visitors

## Navigation

- **Parent:** [[docs/Community Addons/website_livechat/Views]]

