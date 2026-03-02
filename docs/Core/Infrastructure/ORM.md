---
tags: [core, infrastructure, orm]
status: active
---

# ORM

## Focus
- Recordset semantics, environments, caches, prefetching, and domain evaluation.
- Field lifecycle across compute, inverse, onchange, constraints, and flush boundaries.
- Shared write/read patterns that most business addons rely on.

## Odoo 19 API surface
- The public `odoo.api` package exports decorators such as `model`, `model_create_multi`, `depends`, `depends_context`, `constrains`, `onchange`, `ondelete`, `readonly`, `private`, and `autovacuum`.
- The implementation lives under `odoo/orm/decorators.py`, while `odoo/api/__init__.py` controls the public decorator surface exposed to addon code.
- `@api.readonly` is part of the current public API and is relevant when a model method is called through RPC flows that can use a readonly cursor.

## Migration note
- `@api.returns` is not exported by the Odoo 19 `odoo.api` package. Legacy code using it should be reviewed instead of copied forward blindly.
- When validating migrated addon code, treat missing legacy decorators as a signal to re-check the method contract against current ORM behavior rather than assuming a direct decorator replacement exists.

## Related notes
- `[[docs/Core/Framework/http]]` for RPC-facing controller entry points.
- `[[docs/Core/Infrastructure/Community Q&A]]` for validated forum-derived troubleshooting notes.

## Navigation
- **Parent:** [[docs/Core/Infrastructure/Infrastructure]]
