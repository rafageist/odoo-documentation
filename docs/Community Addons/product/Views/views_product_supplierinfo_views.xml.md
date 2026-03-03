---
tags: [odoo, community, generated, views]
---

# views/product_supplierinfo_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_supplierinfo_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_supplierinfo_tree_view`
- Name: product.supplierinfo.list.view
- Model: `product.supplierinfo`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `company_id`, `currency_id`, `date_end`, `date_start`, `delay`, `discount`, `min_qty`, `partner_id`, `price`, `product_code`, and 5 more
- XPath or positional patches: 0

### `product_supplierinfo_view_kanban`
- Name: product.supplierinfo.kanban
- Model: `product.supplierinfo`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `currency_id`, `delay`, `min_qty`, `partner_id`, `price`
- XPath or positional patches: 0

### `product_supplierinfo_search_view`
- Name: product.supplierinfo.search.view
- Model: `product.supplierinfo`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `partner_id`, `product_code`, `product_name`, `product_tmpl_id`
- XPath or positional patches: 0

### `product_supplierinfo_form_view`
- Name: product.supplierinfo.form.view
- Model: `product.supplierinfo`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `company_id`, `currency_id`, `date_end`, `date_start`, `delay`, `discount`, `min_qty`, `partner_id`, `price`, `product_code`, and 5 more
- XPath or positional patches: 0

## Actions

- `product_supplierinfo_type_action`: `act_window` Vendor Pricelists

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

