---
tags: [comparison, services]
status: draft
---
# Services (Project) v18 vs v19

> **Summary:** Captures the main changes to project management between v18 and v19. Cross-reference the Odoo 18 project notes (`[[Odoo 18/Core/Processes/Projects]]`).

## Key observations so far
- Project models adopt explicit names (`ProjectProject`) and rely on `Domain` helpers and new read-group utilities when counting tasks/templates.
- Favorite handling now uses cached favorite sets and `domain='in'` filters, simplifying `_search_is_favorite` logic.
- Task domains combine closed/template flags, and manager domain uses bypass search access with emoji fallback (`👤 Unassigned`) for empty assignments.
- Privacy settings introduce `invited_users` visibility, aligning with portal sharing improvements.
- Feature toggles (`allow_task_dependencies`, `allow_milestones`, `allow_recurring_tasks`) now rely on inverse methods instead of defaulting to user groups.
- Project date constraint defined via `models.Constraint`; milestone computations leverage read-group data for performance.

## Migration hints
- Update custom domains manipulating favorites or teams to the new `Domain` API and boolean logic.
- When extending task counts, account for template filtering differences (template counts are excluded from active projects).
- Replace direct references to `_systray_view` or legacy constraint declarations with the new APIs.
- Ensure privacy-related customizations handle the new `invited_users` visibility option.

## Next steps
- Review `project.task` changes (recurrence, assignees) for service delivery flows.
- Check how rating fields moved to dedicated modules and adjust overrides accordingly.
- Document portal/project collaborator updates once v19 docs are available.


## Navigation
- **Parent:** [[Comparisons]]
