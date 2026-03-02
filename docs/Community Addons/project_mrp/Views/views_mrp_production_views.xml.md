<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mrp_production_views.xml

- Module: [[docs/Community Addons/project_mrp/project_mrp|project_mrp]]
- Scope: Community Addons
- Source file: `views/mrp_production_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mrp_production_form_view_inherit_project_mrp`
- Name: mrp.production.view.inherited
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_form_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `bom_id`, `project_id`
- XPath or positional patches: 1

### `view_production_tree_view_inherit_project_mrp`
- Name: mrp.production.list.view.inherit.project_mrp
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_tree_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `name`, `project_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/project_mrp/Views]]

<!-- GENERATED:VIEWFILE -->
