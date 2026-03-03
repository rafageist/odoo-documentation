---
tags: [odoo, enterprise, generated, views]
---

# views/website_visitor_views.xml

- Module: [[docs/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]
- Scope: Enterprise Addons
- Source file: `views/website_visitor_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `website_visitor_view_search`
- Name: website.visitor.view.search.inherit.social.push.notifications
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `website_visitor_view_kanban`
- Name: website.visitor.view.kanban.inherit.social.push.notifications
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_kanban`
- Root tag: `field`
- Field references: 2
- Sample fields: `country_id`, `has_push_notifications`
- Buttons: `action_send_push_notification`
- XPath or positional patches: 1

### `website_visitor_view_tree`
- Name: website.visitor.view.list.inherit.social.push.notifications
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `has_push_notifications`
- Buttons: `action_send_push_notification`
- XPath or positional patches: 1

### `website_visitor_view_form`
- Name: website.visitor.view.form.inherit.social.push.notifications
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `has_push_notifications`
- Buttons: `action_send_push_notification`
- XPath or positional patches: 2

## Actions

- `social_send_push_notifications_action_server`: `server` Send Push Notifications

## Menus

- `social_visitor`: Visitors

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_push_notifications/Views]]

