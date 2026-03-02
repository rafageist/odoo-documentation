<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# DocController

- Module: [[docs/Community Addons/api_doc/api_doc|api_doc]]
- Scope: Community Addons
- Source file: `controllers/api_doc.py`
- Base classes: `http.Controller`
- Routes: 5

## Routes

### `doc_client`
- Paths: `/doc`, `/doc/<model_name>`, `/doc/index.html`
- Type: `http`
- Auth: `user`

### `doc_bearer_index`
- Paths: `/doc-bearer/index.json`
- Type: `http`
- Auth: `bearer`

### `doc_index`
- Paths: `/doc/index.json`
- Type: `http`
- Auth: `user`

### `doc_bearer_modec`
- Paths: `/doc-bearer/<model_name>.json`
- Type: `http`
- Auth: `bearer`
- Readonly: `True`

### `doc_model`
- Paths: `/doc/<model_name>.json`
- Type: `http`
- Auth: `user`
- Readonly: `True`

## Navigation

- **Parent:** [[docs/Community Addons/api_doc/Controllers]]

<!-- GENERATED:CONTROLLER -->



