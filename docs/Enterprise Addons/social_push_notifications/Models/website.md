<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# website

- Module: [[docs/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/website.py`
- Python classes: `Website`

## Field footprint

- Detected fields: 12
- Field types: `Binary` x 2, `Boolean` x 2, `Char` x 6, `Integer` x 1, `Text` x 1
- Relation fields: 0

## Sample fields

- `firebase_admin_key_file`: `Binary` (comodel `Firebase Admin Key File`)
- `firebase_enable_push_notifications`: `Boolean` (comodel `Enable Web Push Notifications`)
- `firebase_project_id`: `Char` (comodel `Firebase Project ID`)
- `firebase_push_certificate_key`: `Char` (comodel `Firebase Push Certificate Key`)
- `firebase_sender_id`: `Char` (comodel `Firebase Sender ID`)
- `firebase_use_own_account`: `Boolean` (comodel `Use your own Firebase account`)
- `firebase_web_api_key`: `Char` (comodel `Firebase Web API Key`)
- `firebase_web_app_id`: `Char` (comodel `Firebase Web App ID`)
- `notification_request_body`: `Text` (comodel `Notification Request Text`)
- `notification_request_delay`: `Integer` (comodel `Notification Request Delay (seconds)`)
- `notification_request_icon`: `Binary` (comodel `Notification Request Icon`)
- `notification_request_title`: `Char` (comodel `Notification Request Title`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_push_notifications/Models]]

<!-- GENERATED:MODEL -->
