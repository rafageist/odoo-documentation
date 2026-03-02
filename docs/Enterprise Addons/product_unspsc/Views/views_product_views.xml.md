<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_product_unspsc_code_form`
- Name: view.product.unspsc.code.form
- Model: `product.unspsc.code`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `active`, `applies_to`, `code`, `name`
- XPath or positional patches: 0

### `view_product_uom_categ_search_unspsc`
- Name: view.uom.categ.unspsc.search
- Model: `product.unspsc.code`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `code`, `name`
- XPath or positional patches: 0

### `view_product_uom_categ_tree_unspsc`
- Name: view.uom.categ.unspsc.list
- Model: `product.unspsc.code`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `code`, `name`
- XPath or positional patches: 0

### `view_product_uom_form_unspsc`
- Name: view.uom.uom.unspsc.form
- Model: `uom.uom`
- Type: inferred from arch
- Inherits: `uom.product_uom_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `unspsc_code_id`
- XPath or positional patches: 1

### `product_template_unspsc`
- Name: product.template.form.unspsc
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `unspsc_code_id`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/product_unspsc/Views]]

<!-- GENERATED:VIEWFILE -->
