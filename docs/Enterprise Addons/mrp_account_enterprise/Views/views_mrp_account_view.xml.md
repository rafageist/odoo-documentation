---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_account_view.xml

- Module: [[docs/Enterprise Addons/mrp_account_enterprise/mrp_account_enterprise|mrp_account_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/mrp_account_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mrp_workcenter_tree_view_inherited`
- Name: mrp.workcenter.list.inherited
- Model: `mrp.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_workcenter_tree_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `analytic_distribution`
- XPath or positional patches: 1

### `mrp_workcenter_view_inherit`
- Name: mrp.workcenter.form.inherit
- Model: `mrp.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_workcenter_view`
- Root tag: `group`
- Field references: 1
- Sample fields: `analytic_distribution`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_account_enterprise/Views]]

