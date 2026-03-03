---
tags: [odoo, core, integrations, http, rpc]
status: active
---

# HTTP and RPC Contracts

## Scope
- Route-level contracts that external callers and the web client depend on.
- Authentication modes, payload shapes, stateless behavior, and error envelopes.
- The practical difference between classic HTTP responses, `jsonrpc`, `json2`, and the `/json/1/*` export surface.

## Source areas
- `odoo19/odoo/http.py`
- `odoo19/addons/web/controllers/session.py`
- `odoo19/addons/web/controllers/action.py`
- `odoo19/addons/web/controllers/dataset.py`
- `odoo19/addons/web/controllers/json.py`
- `odoo19/odoo/tests/common.py`

## Route contract knobs
- `type="http"` means normal HTTP semantics: query string and form data become params, controllers can return redirects or rendered pages, and CSRF is enabled by default for unsafe methods.
- `type="jsonrpc"` means a JSON-RPC 2.0 envelope over HTTP. Odoo expects named `params`, ignores the JSON-RPC `method` field for routing, and returns either a `result` or an `error` envelope.
- `type="json2"` is a separate dispatcher for raw JSON bodies. It merges the decoded JSON object with path parameters and returns plain JSON with ordinary HTTP status codes instead of a JSON-RPC envelope.
- `auth="bearer"` is the stateless API-oriented mode. The route decorator defaults `save_session=False` there, so the request can authenticate via API key without persisting a browser session.
- The `X-Odoo-Database` header is also stateless. When used without a session cookie, Odoo selects the database from the header and sets `session.can_save = False`. Mixing that header with a conflicting `session_id` cookie is rejected.

## Core backend RPC surfaces

### Session and bootstrap endpoints
- `/web/session/authenticate` is `type="jsonrpc"` with `auth="none"` and `readonly=False` because it can create or renew the authenticated session.
- `/web/session/get_session_info` is `type="jsonrpc"` with `auth="user"` and `readonly=True`; it returns the session payload that the backend shell and web client use for feature flags, menus, and runtime context.
- `/web/session/logout` is `type="http"` with `auth="none"` and returns an HTTP redirect after clearing the session.

### Action and model execution endpoints
- `/web/action/load` is `type="jsonrpc"` with `auth="user"` and `readonly=True`. It resolves an action id or XML id and returns the action structure expected by the client.
- `/web/dataset/call_kw` and `/web/dataset/call_button` are `type="jsonrpc"` with `auth="user"`. Their readonly status is computed dynamically from the target model method's `_readonly` marker before delegating to `odoo.service.model.call_kw(...)`.
- The contract for those routes is not "generic free API". They are web client transport surfaces sitting directly on top of the ORM and current request context.

### `/json/1/*` view export surface
- `/json/<subpath>` is only a browser-friendly redirect to `/json/1/<subpath>`.
- `/json/1/<subpath>` is `type="http"` with `auth="bearer"` and `readonly=True`.
- The route is gated by `base.group_allow_export`.
- It returns a simplified JSON representation of actions and views as they would appear in the client. That makes it useful for export and inspection use cases, not as a generic CRUD API.

## Payload expectations
- The canonical JSON-RPC payload shape used across tests and web controllers is:

```json
{
  "jsonrpc": "2.0",
  "method": "call",
  "id": "client-generated-id",
  "params": {
    "model": "res.partner"
  }
}
```

- `odoo/tests/common.py` exposes `build_rpc_payload()` with that same envelope, which is a strong signal for how custom clients should shape requests.
- In `jsonrpc`, the `params` member must be an object, not a positional array.
- In `json2`, the body itself is the parameter object. There is no JSON-RPC wrapper and no `id` field to echo back.
- Context overrides are still route-specific. For example, some web client controllers accept a `context` key and merge it into `request.context` before calling the target model logic.

## Failure handling
- `type="http"` routes follow ordinary HTTP behavior: redirects stay redirects, `BadRequest` stays an HTTP status, and HTML pages can be rendered for fallback flows.
- `type="jsonrpc"` routes always answer with a JSON-RPC envelope. Odoo uses an `error` object when dispatch fails, including a dedicated `code=100` / `message="Odoo Session Expired"` case for expired sessions.
- `type="json2"` routes serialize exceptions to JSON too, but keep HTTP status semantics. A bad request is still a 400, a missing route can stay 404, and internal failures become 500.
- Invalid JSON on a `jsonrpc` route is rejected before normal endpoint handling with an HTTP 400 response.

## Practical rules
- Use `auth="bearer"` when an integration should not piggyback on a browser session.
- Disable CSRF intentionally on machine-to-machine HTTP callbacks only when the caller is external and another verification mechanism exists.
- Treat `/web/dataset/*` and `/web/action/*` as internal web client contracts. They are stable enough to understand the backend shell, but not a clean external integration API.
- Treat `/json/1/*` as a read-oriented projection layer tied to action/view resolution and export permissions.

## Related notes
- `[[docs/Core/Framework/http]]`
- `[[docs/Core/Framework/auth]]`
- `[[docs/Core/Framework/Runtime Lifecycle]]`

## Navigation
- **Parent:** [[docs/Core/Integrations/Integrations]]
