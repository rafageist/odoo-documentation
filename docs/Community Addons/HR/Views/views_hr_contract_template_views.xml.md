<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_contract_template_views.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/hr_contract_template_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_contract_template_list_view`
- Name: hr.contract.template.list
- Model: `hr.version`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `company_id`, `contract_type_id`, `create_date`, `create_uid`, `currency_id`, `department_id`, `job_id`, `name`, `resource_calendar_id`, `structure_type_id`, and 1 more
- XPath or positional patches: 0

### `hr_contract_template_form_view`
- Name: hr.contract.template.form
- Model: `hr.version`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `contract_type_id`, `currency_id`, `department_id`, `hr_responsible_id`, `job_id`, `name`, `resource_calendar_id`, `structure_type_id`, `wage`
- XPath or positional patches: 0

## Actions

- `action_hr_contract_templates`: `act_window` Contract Templates

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
