<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# Sign

- Module: [[docs/Enterprise Addons/sign/sign|sign]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 20

## Routes

### `share_link`
- Paths: `/sign/<share_link>`
- Type: `http`
- Auth: `public`

### `sign_document_from_mail`
- Paths: `/sign/document/mail/<int:request_id>/<token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `sign_document_public`
- Paths: `/sign/document/<int:sign_request_id>/<token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `download_document`
- Paths: `/sign/download/<int:request_id>/<token>/<download_type>`, `/sign/download/<int:request_id>/<token>/<download_type>/<int:sign_document_id>`
- Type: `http`
- Auth: `public`

### `download_multiple_documents`
- Paths: `/sign/download/zip/<ids>`
- Type: `http`
- Auth: `user`

### `resend_expired_link`
- Paths: `/sign/resend_expired_link/<int:request_id>/<token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_document`
- Paths: `/sign/get_document/<int:request_id>/<token>`
- Type: `jsonrpc`
- Auth: `user`

### `get_original_documents`
- Paths: `/sign/get_original_documents/<int:request_id>/<token>`
- Type: `jsonrpc`
- Auth: `user`

### `get_completed_documents`
- Paths: `/sign/get_completed_documents/<int:request_id>/<token>`
- Type: `jsonrpc`
- Auth: `user`

### `update_signature`
- Paths: `/sign/update_user_signature`
- Type: `jsonrpc`
- Auth: `user`

### `make_public_user`
- Paths: `/sign/send_public/<int:request_id>/<token>`
- Type: `jsonrpc`
- Auth: `public`

### `send_sms`
- Paths: `/sign/send-sms/<int:request_id>/<token>/<phone_number>`
- Type: `jsonrpc`
- Auth: `public`

### `sign`
- Paths: `/sign/sign/<int:sign_request_id>/<token>`, `/sign/sign/<int:sign_request_id>/<token>/<sms_token>`
- Type: `jsonrpc`
- Auth: `public`

### `refuse`
- Paths: `/sign/refuse/<int:sign_request_id>/<token>`
- Type: `jsonrpc`
- Auth: `public`

### `save_location`
- Paths: `/sign/save_location/<int:request_id>/<token>`
- Type: `jsonrpc`
- Auth: `public`

### `render_assets_pdf_iframe`
- Paths: `/sign/render_assets_pdf_iframe`
- Type: `jsonrpc`
- Auth: `public`

### `has_sms_credits`
- Paths: `/sign/has_sms_credits`
- Type: `jsonrpc`
- Auth: `public`

### `get_sign_request_state`
- Paths: `/sign/sign_request_state/<int:request_id>/<token>`
- Type: `jsonrpc`
- Auth: `public`

### `get_sign_request_items`
- Paths: `/sign/sign_request_items`
- Type: `jsonrpc`
- Auth: `public`

### `cancel_sign_request_item_from_mail`
- Paths: `/sign/sign_cancel/<int:item_id>/<token>`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sign/Controllers]]

<!-- GENERATED:CONTROLLER -->
