<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_version_views.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/hr_version_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_version_search_view`
- Name: hr.version.search
- Model: `hr.version`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `department_id`, `employee_id`, `job_id`, `resource_calendar_id`
- XPath or positional patches: 0

### `hr_version_pivot_view`
- Name: hr.version.pivot
- Model: `hr.version`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `date_version`, `wage`
- XPath or positional patches: 0

### `hr_version_graph_view`
- Name: hr.version.graph
- Model: `hr.version`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date_version`, `wage`
- XPath or positional patches: 0

### `hr_version_list_view`
- Name: hr.version.list
- Model: `hr.version`
- Type: inferred from arch
- Root tag: `list`
- Field references: 18
- Sample fields: `additional_note`, `company_id`, `contract_date_end`, `contract_date_start`, `contract_type_id`, `create_date`, `create_uid`, `currency_id`, `date_version`, `department_id`, and 8 more
- XPath or positional patches: 0

## Actions

- `action_hr_version`: `act_window` Employee Records

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
