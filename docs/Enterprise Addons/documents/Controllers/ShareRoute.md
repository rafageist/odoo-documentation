<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# ShareRoute

- Module: [[docs/Enterprise Addons/documents/documents|documents]]
- Scope: Enterprise Addons
- Source file: `controllers/documents.py`
- Base classes: `http.Controller`
- Routes: 15

## Routes

### `pdf_split`
- Paths: `/documents/pdf_split`
- Type: `http`
- Auth: `user`

### `documents_home`
- Paths: `/documents/<access_token>`
- Type: `http`
- Auth: `public`

### `documents_avatar`
- Paths: `/documents/avatar/<access_token>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `documents_content`
- Paths: `/documents/content/<access_token>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `documents_redirect`
- Paths: `/documents/redirect/<access_token>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `documents_touch`
- Paths: `/documents/touch/<access_token>`
- Type: `jsonrpc`
- Auth: `user`

### `documents_thumbnail`
- Paths: `/documents/thumbnail/<access_token>`, `/documents/thumbnail/<access_token>/<int:width>x<int:height>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `documents_thumbnail_textual`
- Paths: `/documents/thumbnail_textual/<access_token>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `documents_update_thumbnail`
- Paths: `/documents/document/<int:document_id>/update_thumbnail`
- Type: `jsonrpc`
- Auth: `user`

### `documents_zip`
- Paths: `/documents/zip`
- Type: `http`
- Auth: `user`

### `documents_download_all_legacy`
- Paths: `/document/download/all/<access_token>`, `/document/download/all/<int:share_id>/<access_token>`
- Type: `http`
- Auth: `public`

### `share_portal`
- Paths: `/document/share/<int:share_id>/<token>`, `/document/share/<token>`
- Type: `http`
- Auth: `public`

### `documents_upload`
- Paths: `/documents/upload/`, `/documents/upload/<access_token>`
- Type: `http`
- Auth: `public`

### `documents_upload_success`
- Paths: `/documents/upload/success`
- Type: `http`
- Auth: `public`

### `documents_upload_traceback`
- Paths: `/documents/upload_traceback`
- Type: `http`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents/Controllers]]

<!-- GENERATED:CONTROLLER -->
