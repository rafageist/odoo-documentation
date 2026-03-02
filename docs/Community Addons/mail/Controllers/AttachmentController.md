<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# AttachmentController

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `controllers/attachment.py`
- Base classes: `ThreadController`
- Routes: 5

## Routes

### `mail_attachment_upload`
- Paths: `/mail/attachment/upload`
- Type: `http`
- Auth: `public`

### `mail_attachment_delete`
- Paths: `/mail/attachment/delete`
- Type: `jsonrpc`
- Auth: `public`

### `mail_attachment_get_zip`
- Paths: `/mail/attachment/zip`
- Type: `http`
- Auth: `public`

### `mail_attachment_pdf_first_page`
- Paths: `/mail/attachment/pdf_first_page/<int:attachment_id>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `mail_attachement_update_thumbnail`
- Paths: `/mail/attachment/update_thumbnail`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/mail/Controllers]]

<!-- GENERATED:CONTROLLER -->
