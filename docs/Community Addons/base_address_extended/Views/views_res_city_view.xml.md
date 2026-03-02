<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_city_view.xml

- Module: [[docs/Community Addons/base_address_extended/base_address_extended|base_address_extended]]
- Scope: Community Addons
- Source file: `views/res_city_view.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_city_filter`
- Name: unnamed
- Model: `res.city`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `country_id`, `name`
- XPath or positional patches: 0

### `view_city_tree`
- Name: res.city.list
- Model: `res.city`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `country_id`, `name`, `state_id`, `zipcode`
- XPath or positional patches: 0

## Actions

- `action_res_city_tree`: `act_window` Cities

## Menus

- `menu_res_city`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/base_address_extended/Views]]

<!-- GENERATED:VIEWFILE -->
