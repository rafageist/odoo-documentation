---
tags: [odoo, enterprise, generated, views]
---

# views/esg_gas_views.xml

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Source file: `views/esg_gas_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `esg_gas_kanban_view`
- Name: esg.gas.kanban
- Model: `esg.gas`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `category`, `global_warming_potential`, `name`
- XPath or positional patches: 0

### `esg_gas_list_view`
- Name: esg.gas.list
- Model: `esg.gas`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `global_warming_potential`, `name`, `sequence`
- XPath or positional patches: 0

### `esg_gas_form_view`
- Name: esg.gas.form
- Model: `esg.gas`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `category`, `code`, `global_warming_potential`, `name`
- XPath or positional patches: 0

## Actions

- `action_esg_gasses_list`: `act_window` Gases

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Views]]

