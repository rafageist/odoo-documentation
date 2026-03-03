<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# AccountDocumentDownloadController

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `controllers/download_docs.py`
- Base classes: `http.Controller`
- Routes: 2

## Routes

### `download_invoice_attachments`
- Paths: `/account/download_invoice_attachments/<models("ir.attachment"):attachments>`
- Type: `http`
- Auth: `user`

### `download_invoice_documents_filetype`
- Paths: `/account/download_invoice_documents/<models("account.move"):invoices>/<string:filetype>`
- Type: `http`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Community Addons/account/Controllers]]

<!-- GENERATED:CONTROLLER -->
