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

## Practical boundaries
- XML view definitions, inheritance, and RNG validation belong to the server side.
- Rendering, controllers, models, and interactive state transitions belong to the web client.
- Public website pages also consume `web` assets, but this note should stay focused on the shared client platform rather than website-only behavior.

## Related notes
- `[[docs/Core/Framework/views]]` for XML view architecture, inheritance, and RNG-backed attributes.
- `[[docs/Core/Framework/http]]` for route types, request dispatch, and auth boundaries.

## Navigation
- **Parent:** [[docs/Core/Framework/Framework]]
