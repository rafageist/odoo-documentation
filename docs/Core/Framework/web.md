---
tags: [core, framework, web]
status: active
---

# web (Core Framework)

## Focus
- OWL web client lifecycle, registries, services, actions, and view rendering.
- Asset bundles, lazy loading, and client-side extension points.
- Browser-facing behavior shared by kanban, list, form, and other interactive views.

## Odoo 19 structure
- `addons/web/__manifest__.py` is the canonical map of the client payload. It defines backend, frontend, minimal frontend, lazy backend, report, and test bundles.
- The backend bundle includes `web/static/src/core/**/*`, `web/static/src/views/**/*`, and `web/static/src/webclient/**/*`, which makes `web` the runtime shell for most business views.
- Graph and pivot code are moved into lazy backend assets, so those view types are loaded on demand instead of in the initial backend payload.

## Extension points verified in source
- Services are registered through `registry.category("services")`. Core examples in Odoo 19 include `orm`, `http`, `notification`, `dialog`, `ui`, and `view`.
- View implementations are registered through `registry.category("views")`. Core registrations include `list`, `form`, `kanban`, and `calendar`.
- The server/client contract is route-driven: controllers such as `/web/dataset/call_kw` and `/web/action/load` feed the client with model data, action metadata, and view payloads.

## Public website boundary
- Public website pages are not just the backend web client mounted on `/shop`; Odoo 19 uses a separate frontend model built around QWeb markup plus `registry.category("public.interactions")`.
- In `website_sale`, the primary public behavior is registered in `static/src/interactions/website_sale.js` on `.oe_website_sale`, while the page skeleton still comes from `views/templates.xml`.
- OWL is present in selected public-facing components such as dialogs, notifications, builder options, and editor utilities, but that does not make the storefront a full OWL SPA by default.
- Documentation rule: if a customization needs SEO, snippets, or server-rendered content to keep working, extend the QWeb + public interactions path first and treat full OWL page replacement as an architectural rewrite.

## Website builder template registration
- Website builder customizations live on top of the `website-plugins` registry and the builder option resources under `addons/website/static/src/builder`.
- Header template selection is not auto-discovered from arbitrary QWeb views. The picker enumerates known templates in `header_template_option.xml`, and the navigation plugin keeps its own explicit key list in `header_navigation_option_plugin.js`.
- Theme activation/reset logic also depends on explicit template lists such as `_header_templates` in `addons/website/models/theme_models.py`.
- Practical implication: adding a custom website header or footer preset requires more than declaring a view. The builder option layer must expose and manage that template if it should appear as a native preset.

## Practical boundaries
- XML view definitions, inheritance, and RNG validation belong to the server side.
- Rendering, controllers, models, and interactive state transitions belong to the web client.
- Public website pages also consume `web` assets, but this note should stay focused on the shared client platform rather than website-only behavior.

## Related notes
- `[[docs/Core/Framework/views]]` for XML view architecture, inheritance, and RNG-backed attributes.
- `[[docs/Core/Framework/http]]` for route types, request dispatch, and auth boundaries.
- `[[docs/Community Addons/website_sale/website_sale|website_sale]]` for storefront-specific runtime behavior and controller surface.

## Navigation
- **Parent:** [[docs/Core/Framework/Framework]]
