---
tags: [odoo, enterprise, generated, views]
---

# views/esg_emission_source_views.xml

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Source file: `views/esg_emission_source_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `emission_source_hierarchy_view`
- Name: emission.source.hierarchy
- Model: `esg.emission.source`
- Type: inferred from arch
- Root tag: `hierarchy`
- Field references: 2
- Sample fields: `name`, `scope`
- XPath or positional patches: 0

### `emission_source_search_view`
- Name: emission.source.search
- Model: `esg.emission.source`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `parent_id`
- XPath or positional patches: 0

### `emission_source_kanban_view`
- Name: emission.source.kanban
- Model: `esg.emission.source`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `name`, `parent_id`, `scope`
- XPath or positional patches: 0

### `emission_source_list_view`
- Name: emission.source.list
- Model: `esg.emission.source`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `name`, `parent_id`, `scope`, `sequence`
- XPath or positional patches: 0

### `emission_source_form_view`
- Name: emission.source.form
- Model: `esg.emission.source`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `activity_flow_direct_indirect`, `activity_flow_indirect_others`, `name`, `parent_id`, `scope`
- XPath or positional patches: 0

## Actions

- `action_view_emission_source`: `act_window` Emission Sources

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Views]]

