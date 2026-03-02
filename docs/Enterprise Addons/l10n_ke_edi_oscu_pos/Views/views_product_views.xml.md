<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_pos/l10n_ke_edi_oscu_pos|l10n_ke_edi_oscu_pos]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_ke_pos_kra_product_list`
- Name: product.product.list.l10n.ke.edi.oscu.pos
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `display_name`, `l10n_ke_origin_country_id`, `l10n_ke_packaging_quantity`, `l10n_ke_packaging_unit_id`, `l10n_ke_product_type_code`, `standard_price`, `taxes_id`, `unspsc_code_id`
- XPath or positional patches: 0

### `product_template_form_view_inherit_account_l10n_ke_edi_oscu_pos`
- Name: product.template.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ke_validation_message`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_pos/Views]]

<!-- GENERATED:VIEWFILE -->
