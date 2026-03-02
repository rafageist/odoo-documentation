<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# HTML_Editor

- Module: [[docs/Community Addons/html_editor/html_editor|html_editor]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 15

## Routes

### `remove`
- Paths: `/html_editor/attachment/remove`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `get_image_info`
- Paths: `/html_editor/get_image_info`, `/web_editor/get_image_info`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `video_url_data`
- Paths: `/html_editor/video_url/data`, `/web_editor/video_url/data`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `add_data`
- Paths: `/html_editor/attachment/add_data`, `/web_editor/attachment/add_data`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `add_url`
- Paths: `/html_editor/attachment/add_url`, `/web_editor/attachment/add_url`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `modify_image`
- Paths: `/html_editor/modify_image/<model("ir.attachment"):attachment>`, `/web_editor/modify_image/<model("ir.attachment"):attachment>`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `save_library_media`
- Paths: `/html_editor/save_library_media`, `/web_editor/save_library_media`
- Type: `jsonrpc`
- Auth: `user`

### `shape`
- Paths: `/html_editor/shape/<module>/<path:filename>`, `/web_editor/shape/<module>/<path:filename>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `image_shape`
- Paths: `/html_editor/image_shape/<string:img_key>/<module>/<path:filename>`, `/web_editor/image_shape/<string:img_key>/<module>/<path:filename>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `generate_text`
- Paths: `/html_editor/generate_text`, `/web_editor/generate_text`
- Type: `jsonrpc`
- Auth: `user`

### `get_ice_servers`
- Paths: `/html_editor/get_ice_servers`, `/web_editor/get_ice_servers`
- Type: `jsonrpc`
- Auth: `user`

### `bus_broadcast`
- Paths: `/html_editor/bus_broadcast`, `/web_editor/bus_broadcast`
- Type: `jsonrpc`
- Auth: `user`

### `link_preview_metadata`
- Paths: `/html_editor/link_preview_external`
- Type: `jsonrpc`
- Auth: `public`

### `link_preview_metadata_internal`
- Paths: `/html_editor/link_preview_internal`
- Type: `jsonrpc`
- Auth: `user`

### `media_library_search`
- Paths: `/html_editor/media_library_search`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/html_editor/Controllers]]

<!-- GENERATED:CONTROLLER -->
