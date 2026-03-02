<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# Binary

- Module: [[docs/Community Addons/web/web|web]]
- Scope: Community Addons
- Source file: `controllers/binary.py`
- Base classes: `http.Controller`
- Routes: 7

## Routes

### `content_filestore`
- Paths: `/web/filestore/<path:_path>`
- Type: `http`
- Auth: `none`

### `content_common`
- Paths: `/web/content`, `/web/content/<int:id>`, `/web/content/<int:id>/<string:filename>`, `/web/content/<string:model>/<int:id>/<string:field>`, `/web/content/<string:model>/<int:id>/<string:field>/<string:filename>`, `/web/content/<string:xmlid>`, `/web/content/<string:xmlid>/<string:filename>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `content_assets`
- Paths: `/web/assets/<string:unique>/<string:filename>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `content_image`
- Paths: `/web/image`, `/web/image/<int:id>`, `/web/image/<int:id>-<string:unique>`, `/web/image/<int:id>-<string:unique>/<int:width>x<int:height>`, `/web/image/<int:id>-<string:unique>/<int:width>x<int:height>/<string:filename>`, `/web/image/<int:id>-<string:unique>/<string:filename>`, `/web/image/<int:id>/<int:width>x<int:height>`, `/web/image/<int:id>/<int:width>x<int:height>/<string:filename>`, `/web/image/<int:id>/<string:filename>`, `/web/image/<string:model>/<int:id>/<string:field>`, and 7 more
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `upload_attachment`
- Paths: `/web/binary/upload_attachment`
- Type: `http`
- Auth: `user`

### `company_logo`
- Paths: `/logo`, `/logo.png`, `/web/binary/company_logo`
- Type: `http`
- Auth: `none`

### `get_fonts`
- Paths: `/web/sign/get_fonts`, `/web/sign/get_fonts/<string:fontname>`
- Type: `jsonrpc`
- Auth: `none`

## Navigation

- **Parent:** [[docs/Community Addons/web/Controllers]]

<!-- GENERATED:CONTROLLER -->
