<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.post.template

- Module: [[docs/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_post_template.py`
- Python classes: `SocialPostTemplate`

## Field footprint

- Detected fields: 9
- Field types: `Binary` x 1, `Boolean` x 3, `Char` x 3, `Html` x 1, `Text` x 1
- Relation fields: 0

## Sample fields

- `display_push_notifications_preview`: `Boolean` (comodel `Display Push Notifications Preview`, compute `_compute_display_push_notifications_preview`)
- `has_push_notifications_account`: `Boolean` (comodel `Has Push Notifications Account`, compute `_compute_has_push_notifications_account`)
- `push_notification_image`: `Binary` (comodel `Push Icon Image`)
- `push_notification_message`: `Text` (comodel `Push Notifications Message`, compute `_compute_message_by_media`, store `True`)
- `push_notification_target_url`: `Char` (comodel `Push Target URL`)
- `push_notification_title`: `Char` (comodel `Push Notification Title`)
- `push_notifications_preview`: `Html` (comodel `Push Notifications Preview`, compute `_compute_push_notifications_preview`)
- `use_visitor_timezone`: `Boolean` (comodel `Send at Visitors' Timezone`)
- `visitor_domain`: `Char`

## Method hints

- Detected methods: 8
- Action methods: none
- Compute methods: `_compute_display_push_notifications_preview`, `_compute_has_push_notifications_account`, `_compute_push_notifications_preview`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_push_notifications/Models]]

<!-- GENERATED:MODEL -->
