<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# SocialPushNotificationsController

- Module: [[docs/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 4

## Routes

### `fetch_push_configuration`
- Paths: `/social_push_notifications/fetch_push_configuration`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `register`
- Paths: `/social_push_notifications/register`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `unregister`
- Paths: `/social_push_notifications/unregister`
- Type: `jsonrpc`
- Auth: `public`

### `social_push_get_notification_image`
- Paths: `/social_push_notifications/social_post/<int:post_id>/push_notification_image`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_push_notifications/Controllers]]

<!-- GENERATED:CONTROLLER -->
