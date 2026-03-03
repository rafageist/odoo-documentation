---
tags: [odoo, enterprise, generated, views]
---

# views/esg_emission_factor_views.xml

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Source file: `views/esg_emission_factor_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `emission_factor_search_view`
- Name: emission.factor.search
- Model: `esg.emission.factor`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `compute_method`, `database_id`, `name`, `source_id`
- XPath or positional patches: 0

### `emission_factor_kanban_view`
- Name: emission.factor.kanban
- Model: `esg.emission.factor`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `database_id`, `esg_emissions_value`, `esg_uncertainty_value`, `name`, `scope_complete_name`, `unit_name`
- XPath or positional patches: 0

### `emission_factor_list_view`
- Name: emission.factor.list
- Model: `esg.emission.factor`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `company_id`, `compute_method`, `database_id`, `esg_emissions_value`, `esg_uncertainty_value`, `name`, `region`, `source_id`, `unit_name`, `valid_from`, and 1 more
- XPath or positional patches: 0

### `emission_factor_form_view`
- Name: emission.factor.form
- Model: `esg.emission.factor`
- Type: inferred from arch
- Root tag: `form`
- Field references: 23
- Sample fields: `account_id`, `activity_type_id`, `assignation_line_ids`, `code`, `company_id`, `compute_method`, `currency_id`, `database_id`, `description`, `esg_emissions_value`, and 13 more
- Buttons: `%(factors_auto_assignment_wizard_action)d`, `action_open_linked_emissions`
- XPath or positional patches: 0

## Actions

- `action_apply_factors_auto_assignment`: `server` Assign Emission Factors
- `action_view_emission_factor`: `act_window` Emission Factors

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Views]]

