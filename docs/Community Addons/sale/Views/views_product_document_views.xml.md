<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_document_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/product_document_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_document_search`
- Name: product.document.search.sale
- Model: `product.document`
- Type: inferred from arch
- Inherits: `product.product_document_search`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 1

### `product_document_list`
- Name: product.document.list.sale
- Model: `product.document`
- Type: inferred from arch
- Inherits: `product.product_document_list`
- Root tag: `field`
- Field references: 2
- Sample fields: `attached_on_sale`, `name`
- XPath or positional patches: 0

### `product_document_kanban`
- Name: product.document.kanban.sale
- Model: `product.document`
- Type: inferred from arch
- Inherits: `product.product_document_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `attached_on_sale`
- XPath or positional patches: 1

### `product_document_form`
- Name: product.document.form.sale
- Model: `product.document`
- Type: inferred from arch
- Inherits: `product.product_document_form`
- Root tag: `sheet`
- Field references: 1
- Sample fields: `attached_on_sale`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

<!-- GENERATED:VIEWFILE -->
