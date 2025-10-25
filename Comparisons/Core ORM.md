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
- Logging namespace updated to `odoo.models` and new constants (e.g., `PREFETCH_MAX`).
- Validators, indexes, and constraints rely on new helper classes; regex utilities simplified.
- Access control exceptions now import `LockError` and reuse `exception_to_unicode`.

## Links
- v18 reference: `[[Odoo 18/Core/Infrastructure/ORM.md]]`
- v19 reference placeholder: `[[Odoo 19/Core/Infrastructure/ORM.md]]` (to be created)

## Next steps
- Produce diff of `odoo/models.py` `_check_access` and `write` flows.
- Document migration guidelines for custom computed fields.
- Update this note once v19 reference docs are imported.
