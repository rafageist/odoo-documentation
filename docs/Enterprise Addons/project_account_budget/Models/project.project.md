<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# project.project

- Module: [[docs/Enterprise Addons/project_account_budget/project_account_budget|project_account_budget]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/project_project.py`
- Python classes: `ProjectProject`

## Field footprint

- Detected fields: 2
- Field types: `Float` x 1, `Monetary` x 1
- Relation fields: 0

## Sample fields

- `total_budget_amount`: `Monetary` (comodel `Total planned amount`, compute `_compute_budget`)
- `total_budget_progress`: `Float` (comodel `Budget Spent`, compute `_compute_budget`)

## Method hints

- Detected methods: 6
- Action methods: `action_view_budget_lines`
- Compute methods: `_compute_budget`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_account_budget/Models]]

<!-- GENERATED:MODEL -->
