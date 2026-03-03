---
tags: [odoo, enterprise, generated, views]
---

# report/esg_carbon_emission_report_views.xml

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Source file: `report/esg_carbon_emission_report_views.xml`
- Views: 5
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `carbon_emission_report_pivot_view`
- Name: carbon.emission.report.pivot
- Model: `esg.carbon.emission.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `date`, `esg_emission_factor_id`, `esg_emissions_value_t`, `scope`, `source_id`
- XPath or positional patches: 0

### `carbon_emission_report_graph_view`
- Name: carbon.emission.report.graph
- Model: `esg.carbon.emission.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `date`, `esg_emissions_value_t`, `scope`
- XPath or positional patches: 0

### `carbon_emission_report_search_view`
- Name: carbon.emission.report.search
- Model: `esg.carbon.emission.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `esg_emission_factor_id`, `move_id`, `name`, `partner_id`
- XPath or positional patches: 0

### `carbon_emission_report_kanban_view`
- Name: carbon.emission.report.kanban
- Model: `esg.carbon.emission.report`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `date`, `esg_emission_factor_id`, `esg_emissions_value`, `name`
- XPath or positional patches: 0

### `carbon_emission_report_list_view`
- Name: carbon.emission.report.list
- Model: `esg.carbon.emission.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 18
- Sample fields: `account_id`, `company_id`, `compute_method`, `currency_id`, `database_id`, `date`, `esg_emission_factor_id`, `esg_emissions_value`, `esg_uncertainty_absolute_value`, `esg_uncertainty_value`, and 8 more
- XPath or positional patches: 0

## Actions

- `action_carbon_emission_report_analytics_views`: `act_window` Carbon Analytics
- `action_offset_emission_report_views`: `act_window` Offset Emissions
- `action_emitted_emission_report_views`: `act_window` Emitted Emissions

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Views]]

