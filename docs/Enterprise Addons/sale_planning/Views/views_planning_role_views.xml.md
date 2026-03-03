---
tags: [odoo, enterprise, generated, views]
---

# views/planning_role_views.xml

- Module: [[docs/Enterprise Addons/sale_planning/sale_planning|sale_planning]]
- Scope: Enterprise Addons
- Source file: `views/planning_role_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_planning_role_view_form_inherit_sale_planning`
- Name: sale.planning.role.form.inherit.sale.planning
- Model: `planning.role`
- Type: inferred from arch
- Inherits: `planning.planning_role_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `product_ids`
- XPath or positional patches: 1

### `sale_planning_role_view_form`
- Name: sale.planning.role.form
- Model: `planning.role`
- Type: inferred from arch
- Inherits: `planning.planning_role_view_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `resource_ids`
- XPath or positional patches: 0

### `planning_role_view_tree_inherit_sale_planning`
- Name: planning.role.list.inherit.sale.planning
- Model: `planning.role`
- Type: inferred from arch
- Inherits: `planning.planning_role_view_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `product_ids`, `resource_ids`
- XPath or positional patches: 1

### `planning_role_view_search_inherit_sale_planning`
- Name: planning.role.search.inherit.sale.planning
- Model: `planning.role`
- Type: inferred from arch
- Inherits: `planning.planning_role_view_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `product_ids`, `resource_ids`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_planning/Views]]

