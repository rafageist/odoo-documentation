---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/mrp_plm/mrp_plm|mrp_plm]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_template_form_view`
- Name: product.template.view.form.inherit.version.plm
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `group`
- Field references: 1
- Sample fields: `version`
- XPath or positional patches: 2

### `product_product_view_form_inherit_plm`
- Name: product.product.view.form.inherit.plm
- Model: `product.product`
- Type: inferred from arch
- Inherits: `mrp.product_product_form_view_bom_button`
- Root tag: `button`
- Field references: 1
- Sample fields: `eco_count`
- Buttons: `action_view_mos`, `mrp_eco_action_product_tmpl`
- XPath or positional patches: 0

### `product_template_view_form_inherit_plm`
- Name: product.template.view.form.inherit.plm
- Model: `product.template`
- Type: inferred from arch
- Inherits: `mrp.product_template_form_view_bom_button`
- Root tag: `button`
- Field references: 1
- Sample fields: `eco_count`
- Buttons: `action_view_mos`, `mrp_eco_action_product_tmpl`
- XPath or positional patches: 0

## Actions

- `mrp_eco_action_product_tmpl`: `act_window` Engineering Change Orders

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_plm/Views]]

