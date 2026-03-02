<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 9
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_view_search_catalog`
- Name: product.view.search.catalog.inherit.purchase
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_search_catalog`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `seller_ids`
- XPath or positional patches: 2

### `product_view_kanban_catalog_purchase_only`
- Name: product.view.kanban.catalog.purchase
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_kanban_catalog`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_template_search_view_purchase`
- Name: product.template.search.purchase
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `categ_id`, `seller_ids`
- XPath or positional patches: 1

### `product_normal_form_view_inherit_purchase`
- Name: product.product.purchase.order
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `div`
- Field references: 2
- Sample fields: `purchased_product_qty`, `uom_name`
- Buttons: `action_view_po`
- XPath or positional patches: 1

### `view_product_template_purchase_buttons_from`
- Name: product.template.purchase.button.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `button`
- Field references: 2
- Sample fields: `purchased_product_qty`, `uom_name`
- Buttons: `action_open_documents`, `action_view_po`
- XPath or positional patches: 0

### `view_product_product_supplier_inherit`
- Name: product.product.form
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `seller_ids`, `variant_seller_ids`
- XPath or positional patches: 0

### `view_product_supplier_inherit`
- Name: product.template.supplier.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `description_purchase`, `purchase_line_warn_msg`, `purchase_method`, `seller_ids`, `variant_seller_ids`
- XPath or positional patches: 5

### `product_product_supplierinfo_tree_view2`
- Name: product.supplierinfo.list.view2.product
- Model: `product.supplierinfo`
- Type: inferred from arch
- Inherits: `purchase.product_supplierinfo_tree_view2`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_supplierinfo_tree_view2`
- Name: product.supplierinfo.list.view2
- Model: `product.supplierinfo`
- Type: inferred from arch
- Inherits: `product.product_supplierinfo_tree_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `company_id`
- XPath or positional patches: 7

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Views]]

<!-- GENERATED:VIEWFILE -->
