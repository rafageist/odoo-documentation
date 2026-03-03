---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_bom_views.xml

- Module: [[docs/Enterprise Addons/mrp_plm/mrp_plm|mrp_plm]]
- Scope: Enterprise Addons
- Source file: `views/mrp_bom_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mrp_bom_tree_view_tree`
- Name: mrp.bom.list.inherit.mrp.plm
- Model: `mrp.bom`
- Type: inferred from arch
- Inherits: `mrp.mrp_bom_tree_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `version`
- XPath or positional patches: 1

### `mrp_bom_view_form_inherit_plm_byproducts`
- Name: mrp.bom.view.form.inherit.plm.byproducts
- Model: `mrp.bom`
- Type: inferred from arch
- Inherits: `mrp_plm.mrp_bom_view_form_inherit_plm`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mrp_bom_view_form_inherit_plm_components`
- Name: mrp.bom.view.form.inherit.plm.components
- Model: `mrp.bom`
- Type: inferred from arch
- Inherits: `mrp_plm.mrp_bom_view_form_inherit_plm`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mrp_bom_view_form_inherit_plm`
- Name: mrp.bom.view.form.inherit.plm
- Model: `mrp.bom`
- Type: inferred from arch
- Inherits: `mrp.mrp_bom_form_view`
- Root tag: `div`
- Field references: 3
- Sample fields: `eco_count`, `ready_to_produce`, `version`
- Buttons: `button_mrp_eco`
- XPath or positional patches: 1

## Actions

- `mrp_bom_action_kanban`: `act_window` Bill of Materials

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_plm/Views]]

