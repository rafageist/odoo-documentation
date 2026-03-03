---
tags: [odoo, core, framework, http]
status: active
---

# http

## Focus
- Request lifecycle, routing, controllers, sessions, and RPC-adjacent HTTP behavior in Odoo
- Security and caching considerations at the HTTP layer

## Source areas
- `odoo19/odoo/http.py`
- `odoo19/addons/web/controllers`
- `odoo19/addons/http_routing`

## Odoo 19 runtime model
- `odoo/http.py` drives requests through `_serve_nodb` or `_serve_db`, then `ir.http._match`, `_authenticate`, `_pre_dispatch`, `_dispatch`, and `_post_dispatch`.
- Route `auth` changes what is available in the request environment:
  - `auth="none"` is for routes that must run before normal database or session bootstrap.
  - `auth="public"` uses the public website user when no authenticated user is present.
  - `auth="user"` assumes an authenticated session.
- `type="http"` is the route type for HTML pages, redirects, file streams, and template rendering.
- `type="jsonrpc"` is the route type used by most web client endpoints in Odoo 19, including `/web/dataset/call_kw`, `/web/action/load`, and `/web/session/*`.

## Design guidance
- Keep controllers thin. Route handlers should validate input, shape the HTTP response, and delegate business rules to models or services.
- Prefer explicit auth and readonly flags. Odoo 19 uses `readonly=True` on many web endpoints to keep read-only RPC flows cheap and predictable.
- Document `/jsonrpc` as legacy compatibility, not as the preferred integration surface. Odoo 19 still ships it, but the core marks `/xmlrpc`, `/xmlrpc/2`, and `/jsonrpc` as deprecated for removal in Odoo 20.
- Server configuration now revolves around `http_port`. If a legacy `xmlrpc_port` setting appears to be ignored during local setup, that is expected in the current codebase.

## Related notes
- `[[docs/Core/Framework/Runtime Lifecycle]]` for the end-to-end ingress, dispatch, retry, and ORM handoff.
- `[[docs/Core/Framework/views]]` for server-side view architecture and inheritance.
- `[[docs/Community Addons/http_routing/http_routing|http_routing]]` for multilingual URLs, slugs, and frontend error pages.
- `[[docs/Community Addons/api_doc/api_doc|api_doc]]` for a concrete JSON documentation surface built on top of controllers.

## Navigation
- **Parent:** [[docs/Core/Framework/Framework]]
