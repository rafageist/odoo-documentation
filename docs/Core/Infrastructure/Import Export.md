---
tags: [odoo, core, infrastructure, import, export]
status: active
---

# Import Export

## Scope
- Import/export behavior that is shared across Odoo modules.
- The security, field-path, and external-id mechanics behind the standard UI flows.
- Practical constraints that developers should understand before blaming a module-specific wizard.

## Odoo 19 baseline
- The user-facing import wizard is backed by `base_import.import`, which parses the file, builds a field tree, validates mappings, and then delegates persistence to the model `load()` path.
- `Model.load(fields, data)` normalizes import field paths with `fix_import_export_id_paths(...)`, sets the import context, and then executes the ORM loading pipeline.
- `Model.export_data(fields_to_export)` uses the same path normalizer before exporting rows, so exported sample data is a reliable way to discover valid field paths for a later import.

## Access and permissions
- Export is gated explicitly: `export_data()` requires either administrator status or membership in `base.group_allow_export`.
- Import does not have a magical bypass. Once the parsed rows hit the ORM, normal access checks still apply unless code enters `sudo()` or another privileged execution context.
- For Odoo 19, the relevant security chain is `check_access()` and `_check_access()`, not the legacy `check_access_rule()` helper.

## Record rules and import failures
- A broken or over-restrictive `ir.rule` can surface as an import problem even when the user can open the model in the UI.
- Multi-company filters are part of the same diagnosis, because record-rule domains are computed against the current environment and company scope.
- If a custom module changes grants or injects restrictive record rules, import failures can appear on standard models such as activities without any bug in `base_import`.

## External IDs
- The logical import column `id` is treated as the External ID path during import/export normalization.
- Odoo 19 rejects imported external ids that use the prefix of an installed module, because those records could later be treated as module-owned data.
- For imported business data, `__import__.record_key` is the safe default prefix when a namespaced external id is needed.

## Practical workflow
- If an import fails, first export a small set of valid records from the same model and compare the produced columns with the intended file.
- Use the exported sample to confirm field paths, relational column syntax, and which values the current database already accepts.
- If the same sample still fails on re-import, inspect custom record rules, ACL changes, and company constraints before concluding that the import engine changed.

## Related notes
- `[[docs/Core/Infrastructure/Security]]`
- `[[docs/Core/Infrastructure/Community Q&A]]`

## Navigation
- **Parent:** [[docs/Core/Infrastructure/Infrastructure]]
