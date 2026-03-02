<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_stage_views.xml

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Source file: `views/crm_stage_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `crm_stage_form`
- Name: crm.stage.form
- Model: `crm.stage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `color`, `fold`, `is_won`, `name`, `requirements`, `rotting_threshold_days`, `team_count`, `team_ids`
- XPath or positional patches: 0

### `crm_stage_tree`
- Name: crm.stage.list
- Model: `crm.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `color`, `is_won`, `name`, `rotting_threshold_days`, `sequence`, `team_ids`
- XPath or positional patches: 0

### `crm_lead_stage_search`
- Name: Stage - Search
- Model: `crm.stage`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `is_won`, `name`, `sequence`, `team_ids`
- XPath or positional patches: 0

## Actions

- `crm_stage_action`: `act_window` Stages

## Navigation

- **Parent:** [[docs/Community Addons/crm/Views]]

<!-- GENERATED:VIEWFILE -->
