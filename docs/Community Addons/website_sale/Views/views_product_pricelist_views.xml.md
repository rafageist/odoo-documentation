---
tags: [odoo, community, generated, views]
---

# views/product_pricelist_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/product_pricelist_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `website_sale_pricelist_tree_view`
- Name: product.pricelist.list.inherit.product
- Model: `product.pricelist`
- Type: inferred from arch
- Inherits: `product.product_pricelist_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `currency_id`, `selectable`, `website_id`
- XPath or positional patches: 0

### `website_sale_pricelist_form_view`
- Name: website_sale.pricelist.form
- Model: `product.pricelist`
- Type: inferred from arch
- Inherits: `product.product_pricelist_view`
- Root tag: `notebook`
- Field references: 4
- Sample fields: `code`, `company_id`, `selectable`, `website_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

