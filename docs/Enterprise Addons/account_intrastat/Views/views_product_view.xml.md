---
tags: [odoo, enterprise, generated, views]
---

# views/product_view.xml

- Module: [[docs/Enterprise Addons/account_intrastat/account_intrastat|account_intrastat]]
- Scope: Enterprise Addons
- Source file: `views/product_view.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_intrastat_product_tree`
- Name: product.account.intrastat.list.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_product_tree_view`
- Root tag: `field`
- Field references: 5
- Sample fields: `intrastat_code_id`, `intrastat_origin_country_id`, `intrastat_supplementary_unit`, `intrastat_supplementary_unit_amount`, `type`
- XPath or positional patches: 0

### `product_product_tree_view_account_intrastat_weight`
- Name: product.product.list.account.intrastat
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `default_code`, `intrastat_code_id`, `name`, `weight`
- XPath or positional patches: 0

### `product_product_tree_view_account_intrastat_supplementary_unit`
- Name: product.product.list.account.intrastat
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `default_code`, `intrastat_code_id`, `intrastat_supplementary_unit`, `intrastat_supplementary_unit_amount`, `name`
- XPath or positional patches: 0

### `product_product_tree_view_account_intrastat`
- Name: product.product.list.account.intrastat
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `default_code`, `intrastat_code_id`, `name`
- XPath or positional patches: 0

### `product_product_form_view_inherit_account_intrastat`
- Name: product.product.form.inherit.account.intrastat
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_variant_easy_edit_view`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `intrastat_code_id`, `intrastat_origin_country_id`, `intrastat_supplementary_unit`, `intrastat_supplementary_unit_amount`, `weight`, `weight_uom_name`
- XPath or positional patches: 1

### `product_template_form_view_inherit_account_intrastat`
- Name: product.template.form.inherit.account.intrastat
- Model: `product.template`
- Type: inferred from arch
- Inherits: `account.product_template_form_view`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `intrastat_code_id`, `intrastat_origin_country_id`, `intrastat_supplementary_unit`, `intrastat_supplementary_unit_amount`, `weight`, `weight_uom_name`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_intrastat/Views]]

