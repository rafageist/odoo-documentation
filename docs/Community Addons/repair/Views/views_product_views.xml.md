---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/repair/repair|repair]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_view_search_catalog`
- Name: product.view.search.catalog.inherit.repair
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_search_catalog`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_product_template_form_inherit_repair`
- Name: product.template.form.inherit.repair
- Model: `product.template`
- Type: inferred from arch
- Inherits: `sale.product_template_form_view`
- Root tag: `field`
- Field references: 1
- Sample fields: `service_tracking`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/repair/Views]]

