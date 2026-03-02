---
tags: [odoo, core, infrastructure, q-and-a]
status: active
---

# Community Q&A

## Scope
- This note captures Odoo 19 takeaways mined from the public `Odoo Developers` Telegram archive under `D:\Odoo Developers`.
- Community answers are never treated as source of truth by themselves; each accepted item here has been rechecked against the current Odoo 19 code in this workspace.
- Use `tools/extract_telegram_odoo19.py` to refresh candidate threads before curating new entries.

## Archive boundary
- The earliest explicit Odoo 19 mention found in the current archive set is on `2024-10-10` in the historical export.
- The archive also contains many false positives when searching for plain `19`, so extraction should stay anchored to explicit forms such as `Odoo 19`, `odoo19`, or `v19`.

## Validated takeaways

### Config port key in Odoo 19
- Community prompt: a local setup ignored `xmlrpc_port` while still listening on the default port.
- Validated conclusion: current Odoo 19 configuration uses `http_port`, not `xmlrpc_port`.
- Evidence:
  - `odoo19/odoo/tools/config.py` exposes `-p` and `--http-port` with destination `http_port`.
  - `odoo19/odoo/service/server.py` binds the HTTP server using `config['http_port']`.
  - No active `xmlrpc_port` configuration key was found in the current Odoo 19 source tree.
- Related note: `[[docs/Core/Framework/http]]`

### Legacy `@api.returns` should not be assumed to exist
- Community prompt: a developer asked what replaces `@api.returns` in Odoo 19.
- Validated conclusion: `odoo.api` in Odoo 19 does not export `returns` as part of the public decorator set.
- Evidence:
  - `odoo19/odoo/api/__init__.py` exports `model`, `model_create_multi`, `depends`, `depends_context`, `constrains`, `onchange`, `ondelete`, `readonly`, `private`, and `autovacuum`.
  - `odoo19/odoo/orm/decorators.py` contains the current decorator implementations and no public `returns` decorator.
- Documentation impact: migration notes and custom addon reviews should treat `@api.returns` usage as legacy code that needs revalidation.
- Related note: `[[docs/Core/Infrastructure/ORM]]`

### `product_packaging_qty` was not removed from the current codebase
- Community prompt: a thread claimed that `product_packaging_qty` had been discontinued in Odoo 19.
- Validated conclusion: that claim does not match the current Odoo 19 source tree in this workspace.
- Evidence:
  - The field still appears in `sale`, `purchase`, and `stock` translation catalogs and model-facing code paths.
  - The current addon trees still reference `field_sale_order_line__product_packaging_qty`, `field_purchase_order_line__product_packaging_qty`, and stock equivalents.
- Documentation impact: do not document a replacement field unless a concrete removal is confirmed in the active source tree or in an upstream change set.

## Curation rule
- If a Telegram answer cannot be tied back to code, tests, or official documentation, keep it out of canonical notes and leave it as an extraction candidate only.

## Navigation
- **Parent:** [[docs/Core/Infrastructure/Infrastructure]]
