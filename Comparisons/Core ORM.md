---
tags: [comparison, core, orm]
status: draft
---
# Core ORM v18 vs v19

> **Summary:** Tracks structural changes in the ORM between Odoo 18 and 19 so migration tasks can reference the detailed architecture note `[[Odoo 18/Core/Infrastructure/ORM.md]]`.

## Areas to verify
- **Prefetch & caching:** confirm whether v19 introduces new lazy-loading strategies that affect computed field invalidation.
- **Onchange/Command API:** review `odoo/fields.py` for additions to `Command` helpers or onchange payloads.
- **Queueing & autovacuum:** compare decorators (`@api.autovacuum`) and background hooks.
- **Security integration:** ensure `_check_access` contract matches the updates documented in `[[Odoo 18/Core/Infrastructure/Security.md]]`.

## Structural changes spotted
- ORM code relocated under `odoo/orm/` with `models` exposed via package imports; legacy `odoo/models.py` kept as shim.
- Introduction of dedicated modules (`commands`, `domains`, `fields_*`) with stricter typing hints (`Domain`, `Id`, `Collection`).
- Logging namespace updated to `odoo.models`, introducing extra telemetry for ORM operations.
- Validators, indexes, and constraints rely on new helper classes; regex utilities simplified.
- Access control exceptions now import `LockError` and reuse `exception_to_unicode`.
- Load/unload helpers now live in dedicated modules (`commands`, `domains`, `fields_misc`, `fields_temporal`, etc.), clarifying import points for custom models.
- New constants such as `NO_ACCESS` and `PREFETCH_MAX` influence access control shortcuts and cache sizing.
- Legacy `regex_*` checks and validation utilities are simplified; model/index declarations prefer `models.Constraint`/`models.Index` even inside the ORM.
- Exception surface adds `LockError` handling and uses `exception_to_unicode`, affecting custom overrides of locking logic.

## Links
- v18 reference: `[[Odoo 18/Core/Infrastructure/ORM.md]]`
- v19 reference placeholder: `[[Odoo 19/Core/Infrastructure/ORM.md]]` (to be created)

## Migration checklist
- Update imports in custom modules to the new `odoo.orm` structure (e.g., `from odoo.orm.models import Model`).
- Replace direct access to helper functions (`check_object_name`, `regex_*`) with the new utility APIs where needed.
- Audit overrides relying on `_context` to ensure `env.context` usage aligns with v19 expectations.

## Next steps
- Produce diff of `odoo/models.py` `_check_access` and `write` flows.
- Document migration guidelines for custom computed fields.
- Update this note once v19 reference docs are imported.


## Navigation
- **Parent:** [[Comparisons/Comparisons]]
