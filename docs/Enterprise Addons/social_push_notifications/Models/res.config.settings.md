<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 12
- Field types: `Binary` x 2, `Boolean` x 2, `Char` x 6, `Integer` x 1, `Text` x 1
- Relation fields: 0

## Sample fields

- `firebase_admin_key_file`: `Binary` (comodel `Firebase Admin Key File`, related `website_id.firebase_admin_key_file`)
- `firebase_enable_push_notifications`: `Boolean` (comodel `Enable Web Push Notifications`, related `website_id.firebase_enable_push_notifications`)
- `firebase_project_id`: `Char` (comodel `Firebase Project ID`, related `website_id.firebase_project_id`)
- `firebase_push_certificate_key`: `Char` (comodel `Firebase Push Certificate Key`, related `website_id.firebase_push_certificate_key`)
- `firebase_sender_id`: `Char` (comodel `Firebase Sender ID`, related `website_id.firebase_sender_id`)
- `firebase_use_own_account`: `Boolean` (comodel `Use your own Firebase account`, related `website_id.firebase_use_own_account`)
- `firebase_web_api_key`: `Char` (comodel `Firebase Web API Key`, related `website_id.firebase_web_api_key`)
- `firebase_web_app_id`: `Char` (comodel `Firebase Web App ID`, related `website_id.firebase_web_app_id`)
- `notification_request_body`: `Text` (comodel `Notification Request Text`, related `website_id.notification_request_body`)
- `notification_request_delay`: `Integer` (comodel `Notification Request Delay (seconds)`, related `website_id.notification_request_delay`)
- `notification_request_icon`: `Binary` (comodel `Notification Request Icon`, related `website_id.notification_request_icon`)
- `notification_request_title`: `Char` (comodel `Notification Request Title`, related `website_id.notification_request_title`)

## Method hints

- Detected methods: 0
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_push_notifications/Models]]

<!-- GENERATED:MODEL -->
