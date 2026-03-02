<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# project.template.create.wizard

- Module: [[docs/Enterprise Addons/databases/databases|databases]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `wizard/project_template_create_wizard.py`
- Python classes: `ProjectTemplateCreateWizard`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 3, `Char` x 4, `Selection` x 1
- Relation fields: 0

## Sample fields

- `database_api_key`: `Char`
- `database_api_login`: `Char`
- `database_fetch_documents`: `Boolean` (comodel `Fetch Documents`)
- `database_fetch_draft_entries`: `Boolean` (comodel `Fetch Draft Journal Entries`)
- `database_fetch_tax_returns`: `Boolean` (comodel `Fetch Tax Returns`)
- `database_hosting`: `Selection`
- `database_name`: `Char`
- `database_url`: `Char`

## Method hints

- Detected methods: 2
- Action methods: `action_open_template_view`
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/databases/Models]]

<!-- GENERATED:MODEL -->
