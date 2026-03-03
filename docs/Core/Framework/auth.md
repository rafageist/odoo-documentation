---
tags: [core, framework, auth]
status: active
---

# auth_* (Core Framework)

## Focus
- Authentication entry points across password, OAuth, TOTP, passkeys, and portal/public flows.
- Session establishment, cookie handling, and user elevation boundaries.
- Shared hooks used by `auth_signup`, `auth_oauth`, `auth_totp`, and related addons.

## Odoo 19 auth boundary
- `ir.http._authenticate(...)` is the point where route-level auth becomes safe to rely on. Anything before that should be treated as pre-auth bootstrap code.
- `auth="none"` keeps the route outside normal authenticated guarantees. It is used for database selection, login, health checks, and backend shell bootstrap compatibility.
- `auth="public"` resolves the request to the website/public user when no logged-in session is present.
- `auth="user"` requires a valid non-public session and raises `SessionExpiredException` otherwise.
- `auth="bearer"` validates an API key from the `Authorization: Bearer ...` header and disables session persistence for that request.

## Session handling
- `security.check_session(...)` is the gate that revalidates the stored session against the current environment.
- `web.controllers.home.Home.web_client` uses `auth="none"` but then explicitly restores the user with `request.update_env(user=request.session.uid)` after checking the session. That route is a bootstrap exception, not a pattern to copy blindly into custom controllers.
- `Dispatcher.pre_dispatch(...)` can turn off session persistence when the route sets `save_session=False`.
- `Dispatcher.post_dispatch(...)` is where the session is actually saved back and response headers are injected.

## Practical rules
- Do not use `auth="none"` as a shortcut for custom APIs that need ORM access. Use `auth="user"`, `auth="public"`, or `auth="bearer"` intentionally.
- If a route needs to be stateless, combine the right auth mode with `save_session=False`; do not rely on developers remembering not to touch `request.session`.
- Session-expired behavior differs by dispatcher: HTTP routes typically redirect to login, while JSON-RPC routes encode a structured session-expired error.

## Related notes
- `[[docs/Core/Framework/http]]`
- `[[docs/Core/Framework/Runtime Lifecycle]]`

## Navigation
- **Parent:** [[docs/Core/Framework/Framework]]
