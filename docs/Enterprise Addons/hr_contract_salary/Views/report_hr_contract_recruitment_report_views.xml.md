---
tags: [odoo, enterprise, generated, views]
---

# report/hr_contract_recruitment_report_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `report/hr_contract_recruitment_report_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `contract_recruitment_report_view_list`
- Name: contract.recruitment.report.view.list
- Model: `hr.contract.recruitment.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `applicant_id`, `job_id`, `offer_create_date`, `offer_id`, `offer_state`
- XPath or positional patches: 0

### `contract_recruitment_report_view_pivot`
- Name: contract.recruitment.report.view.pivot
- Model: `hr.contract.recruitment.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `job_id`, `offer_state`
- XPath or positional patches: 0

### `contract_recruitment_report_view_graph`
- Name: contract.recruitment.report.view.graph
- Model: `hr.contract.recruitment.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `job_id`, `offer_state`
- XPath or positional patches: 0

### `contract_recruitment_report_view_search`
- Name: contract.recruitment.report.view.search
- Model: `hr.contract.recruitment.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `job_id`, `offer_create_date`
- XPath or positional patches: 0

## Actions

- `contract_recruitment_report_action`: `act_window` Offer Analysis

## Menus

- `menu_report_contract_recruitment_all`: Offer Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Views]]

