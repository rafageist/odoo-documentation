---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_product_form__view_inherit_l10n_ke_edi_oscu`
- Name: product.product.form.inherit.l10n.ke.edi.oscu.stock
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_variant_easy_edit_view`
- Root tag: `button`
- Field references: 0
- Buttons: `action_l10n_ke_oscu_save_item`, `action_l10n_ke_oscu_save_stock_master`
- XPath or positional patches: 0

### `product_template_form_view_inherit_account_l10n_ke_edi_oscu`
- Name: product.template.form.inherit.account.l10n.ke.edi.oscu.stock
- Model: `product.template`
- Type: inferred from arch
- Inherits: `account.product_template_form_view`
- Root tag: `button`
- Field references: 0
- Buttons: `action_l10n_ke_oscu_save_item`, `action_l10n_ke_oscu_save_stock_master`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/Views]]

