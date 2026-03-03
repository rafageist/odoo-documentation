---
tags: [odoo, core, infrastructure, q-and-a]
status: active
---

# Community Q&A

## Scope
- This note captures Odoo 19 takeaways mined from the public `Odoo Developers` Telegram archive under `D:\Odoo Developers`.
- Community answers are never treated as source of truth by themselves; each accepted item here has been rechecked against the current Odoo 19 code in this workspace.
- Use `tools/extract_telegram_odoo19.py` to refresh candidate threads before curating new entries.
- For topic-driven curation, prefer structured extraction such as `python tools/extract_telegram_odoo19.py --topic website --topic owl --topic website_sale --format json`.

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

### `website_sale` is not a full OWL storefront by default
- Community prompt: a developer wanted to replace the Odoo 19 `website_sale` product page with a frontend built entirely in OWL.
- Validated conclusion: the public storefront in Odoo 19 is still primarily server-rendered with QWeb and then enhanced with `public.interactions`; OWL exists in targeted components, but not as the default rendering shell for `/shop`.
- Evidence:
  - `odoo19/addons/website_sale/views/templates.xml` still defines the product-page and storefront QWeb structure.
  - `odoo19/addons/website_sale/__manifest__.py` loads `website_sale/static/src/interactions/**/*` into `web.assets_frontend`, which is the main public runtime path.
  - `odoo19/addons/website_sale/static/src/interactions/website_sale.js` registers `.oe_website_sale` as a `registry.category('public.interactions')` behavior.
  - OWL is present in focused pieces such as `website_sale/static/src/js/components/website_sale_image_viewer.js` and notification components, not as the default page container.
- Documentation impact: a full OWL rewrite of the product page should be treated as a custom architecture decision with SEO, snippet compatibility, and maintenance tradeoffs.
- Related notes: `[[docs/Core/Framework/web]]`, `[[docs/Community Addons/website_sale/website_sale|website_sale]]`

### Website builder header templates are explicitly registered
- Community prompt: a custom Odoo 19 website header template did not appear in the builder dropdown even though the module depended on `website`.
- Validated conclusion: the builder does not auto-discover new header templates from QWeb views alone; the dropdown and activation logic enumerate known template keys explicitly.
- Evidence:
  - `odoo19/addons/website/static/src/builder/plugins/options/header/header_template_option.xml` defines the selectable header items with hardcoded `views` payloads.
  - `odoo19/addons/website/static/src/builder/plugins/options/header/header_navigation_option_plugin.js` keeps an explicit `this.keys` list of header template view keys.
  - `odoo19/addons/website/models/theme_models.py` also keeps `_header_templates` as an explicit whitelist for theme reset and toggle logic.
- Documentation impact: declaring a new `template_header_*` view and depending on `website` is necessary but not sufficient; custom header templates also need builder option integration if they should appear and behave like first-class presets.
- Related notes: `[[docs/Core/Framework/web]]`

## Curation rule
- If a Telegram answer cannot be tied back to code, tests, or official documentation, keep it out of canonical notes and leave it as an extraction candidate only.

## Navigation
- **Parent:** [[docs/Core/Infrastructure/Infrastructure]]
