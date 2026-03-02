<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/uom_uom_views.xml

- Module: [[docs/Community Addons/uom/uom|uom]]
- Scope: Community Addons
- Source file: `views/uom_uom_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `uom_uom_view_search`
- Name: uom.uom.view.search
- Model: `uom.uom`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `product_uom_form_view`
- Name: uom.uom.form
- Model: `uom.uom`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `name`, `relative_factor`, `relative_uom_id`
- XPath or positional patches: 0

### `product_uom_tree_view`
- Name: uom.uom.list
- Model: `uom.uom`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `name`, `relative_factor`, `relative_uom_id`, `sequence`
- XPath or positional patches: 0

## Actions

- `product_uom_form_action`: `act_window` Units & Packagings

## Navigation

- **Parent:** [[docs/Community Addons/uom/Views]]

<!-- GENERATED:VIEWFILE -->
