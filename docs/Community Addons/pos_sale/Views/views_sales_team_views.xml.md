<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/sales_team_views.xml

- Module: [[docs/Community Addons/pos_sale/pos_sale|pos_sale]]
- Scope: Community Addons
- Source file: `views/sales_team_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_pos_config_search_inherit_pos_sale`
- Name: pos.config.search.view
- Model: `pos.config`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_config_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `crm_team_id`
- XPath or positional patches: 1

### `view_pos_session_search_inherit_pos_sale`
- Name: pos.session.search.view
- Model: `pos.session`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_session_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `crm_team_id`
- XPath or positional patches: 1

## Actions

- `pos_session_action_from_crm_team`: `act_window` Open Sessions

## Navigation

- **Parent:** [[docs/Community Addons/pos_sale/Views]]

<!-- GENERATED:VIEWFILE -->
