<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/sale_project/sale_project|sale_project]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_product_form_view_inherit_sale_project`
- Name: product.product.sale.project.form
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `field`
- Field references: 1
- Sample fields: `type`
- XPath or positional patches: 0

### `product_template_form_view_inherit_sale_project`
- Name: product.template.sale.project.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `sale.product_template_form_view`
- Root tag: `field`
- Field references: 1
- Sample fields: `type`
- XPath or positional patches: 0

### `product_template_form_view_invoice_policy_inherit_sale_project`
- Name: product.template.inherit.sale.projectform
- Model: `product.template`
- Type: inferred from arch
- Inherits: `sale.product_template_form_view`
- Root tag: `field`
- Field references: 6
- Sample fields: `invoice_policy`, `project_id`, `project_template_id`, `service_policy`, `service_tracking`, `task_template_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/sale_project/Views]]

<!-- GENERATED:VIEWFILE -->
