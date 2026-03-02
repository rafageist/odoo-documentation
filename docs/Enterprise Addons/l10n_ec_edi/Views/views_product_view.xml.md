<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_view.xml

- Module: [[docs/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]]
- Scope: Enterprise Addons
- Source file: `views/product_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_product_product_auxiliary_codes_form`
- Name: view.product.product.auxiliary.codes.form
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ec_auxiliary_code`
- XPath or positional patches: 1

### `view_product_template_auxiliary_codes_form`
- Name: view.product.template.auxiliary.codes.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ec_auxiliary_code`
- XPath or positional patches: 1

### `view_product_template_withhold_form`
- Name: view.product.template.withhold.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `account.product_template_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ec_withhold_tax_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ec_edi/Views]]

<!-- GENERATED:VIEWFILE -->
