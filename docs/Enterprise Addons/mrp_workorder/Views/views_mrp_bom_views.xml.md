<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_bom_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]]
- Scope: Enterprise Addons
- Source file: `views/mrp_bom_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mrp_routing_workcenter_bom_tree_view`
- Name: mrp.routing.workcenter.bom.list.view.inherited
- Model: `mrp.routing.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_routing_workcenter_bom_tree_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mrp_bom_form_view_inherited`
- Name: mrp.bom.from.inherited
- Model: `mrp.bom`
- Type: inferred from arch
- Inherits: `mrp.mrp_bom_form_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `operation_count`, `quality_point_count`
- Buttons: `%(mrp.mrp_routing_action)d`
- XPath or positional patches: 1

### `mrp_routing_workcenter_tree_view_inherited`
- Name: mrp.routing.workcenter.list.view.inherited
- Model: `mrp.routing.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_routing_workcenter_tree_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `quality_point_count`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder/Views]]

<!-- GENERATED:VIEWFILE -->
