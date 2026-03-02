<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mrp_production_views.xml

- Module: [[docs/Community Addons/mrp_account/mrp_account|mrp_account]]
- Scope: Community Addons
- Source file: `views/mrp_production_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_production_graph_inherit_mrp_account`
- Name: mrp.production.graph.inherited.mrp.account
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.view_production_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `extra_cost`
- XPath or positional patches: 1

### `mrp_production_form_view_inherited`
- Name: mrp.production.view.inherited
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_form_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `show_valuation`, `wip_move_count`
- Buttons: `action_view_move_wip`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/mrp_account/Views]]

<!-- GENERATED:VIEWFILE -->
