---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/l10n_pe_reports_stock/l10n_pe_reports_stock|l10n_pe_reports_stock]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_product_stock_tree`
- Name: product.product.stock.list.inherit.l10n_pe_reports_stock
- Model: `product.product`
- Type: inferred from arch
- Inherits: `stock.product_product_stock_tree`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_get_pe_ple_reports`
- XPath or positional patches: 1

### `product_template_form_view_inherit`
- Name: product.template.form.view.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_pe_type_of_existence`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_pe_reports_stock/Views]]

