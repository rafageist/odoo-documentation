---
tags: [odoo, enterprise, generated, views]
---

# views/utm_campaign_views.xml

- Module: [[docs/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]
- Scope: Enterprise Addons
- Source file: `views/utm_campaign_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `utm_campaign_view_kanban`
- Name: utm.campaign.view.kanban.inherit.push_notifications
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `social_push_notifications_count`
- XPath or positional patches: 1

### `utm_campaign_view_form`
- Name: utm.campaign.view.form.inherit.push_notifications
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `social_push_notification_ids`, `social_push_notifications_count`
- Buttons: `action_redirect_to_push_notifications`, `action_send_push_notification`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_push_notifications/Views]]

