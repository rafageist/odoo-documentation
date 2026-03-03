---
tags: [core, infrastructure, seguridad]
status: backlog
---

# Security

## Focus
- Group membership, ACLs, record rules, and multi-company isolation.
- Authorization order across public routes, user context, sudo, and implied groups.
- Security primitives that surface in both backend views and automated jobs.

## Odoo 19 baseline
- Model access starts with `ir.model.access` and then applies record rules through `ir.rule`.
- The current ORM path is `check_access()` -> `_check_access()`. Documentation and custom code should not keep teaching `check_access_rule()` as the primary API because it is deprecated since 18.0.
- `_check_access()` first verifies model-level permission with `ir.model.access.check(...)` and then computes the effective record-rule domain with `ir.rule._compute_domain(...)`.
- `sudo()` still bypasses those checks because the short circuit is `env.su`, not group membership alone.

## Record rules in operational flows
- Record rules are not a backend-only concern. They also affect imports, exports, portal actions, scheduled jobs, and any controller code that stays on the regular user environment.
- When a functional administrator reports that an import fails, treat custom record rules and multi-company filters as part of the first-pass diagnosis instead of assuming an import wizard bug.
- Use `[[docs/Core/Infrastructure/Import Export]]` when the failure happens in CSV/XLSX flows, because the import pipeline eventually lands on normal ORM access checks.

## Diagrams
- Access-evaluation order for a model operation.

## Navigation
- **Parent:** [[docs/Core/Infrastructure/Infrastructure]]
