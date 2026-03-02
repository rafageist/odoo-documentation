<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu/l10n_ke_edi_oscu|l10n_ke_edi_oscu]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_product_ke_code_search`
- Name: product.template.ke.code.search
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_ke_item_code`, `name`
- XPath or positional patches: 0

### `product_template_tree_view_inherit_l10n_ke_edi_oscu`
- Name: product.template.list.inherit.l10n.ke.edi.oscu
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `barcode`, `l10n_ke_item_code`
- XPath or positional patches: 0

### `l10n_ke_kra_product_tree`
- Name: product.product.list.l10n.ke.edi.oscu
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `display_name`, `l10n_ke_item_code`, `l10n_ke_origin_country_id`, `l10n_ke_packaging_quantity`, `l10n_ke_packaging_unit_id`, `l10n_ke_product_type_code`, `standard_price`, `taxes_id`, `unspsc_code_id`
- XPath or positional patches: 0

### `product_product_form__view_inherit_l10n_ke_edi_oscu`
- Name: product.product.form.inherit.l10n.ke.edi.oscu
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_variant_easy_edit_view`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `fiscal_country_codes`, `l10n_ke_is_insurance_applicable`, `l10n_ke_item_code`, `l10n_ke_origin_country_id`, `l10n_ke_packaging_quantity`, `l10n_ke_packaging_unit_id`, `l10n_ke_product_type_code`
- Buttons: `action_l10n_ke_oscu_save_item`
- XPath or positional patches: 1

### `product_template_form_view_inherit_account_l10n_ke_edi_oscu`
- Name: product.template.form.inherit.account.l10n.ke.edi.oscu
- Model: `product.template`
- Type: inferred from arch
- Inherits: `account.product_template_form_view`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `l10n_ke_is_insurance_applicable`, `l10n_ke_item_code`, `l10n_ke_origin_country_id`, `l10n_ke_packaging_quantity`, `l10n_ke_packaging_unit_id`, `l10n_ke_product_type_code`
- Buttons: `action_l10n_ke_oscu_save_item`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu/Views]]

<!-- GENERATED:VIEWFILE -->
