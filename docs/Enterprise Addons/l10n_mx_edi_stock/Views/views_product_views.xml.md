<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi_stock/l10n_mx_edi_stock|l10n_mx_edi_stock]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_template_unspsc_l10n_mx_stock`
- Name: view.uom.categ.unspsc.code.form.l10n_mx_stock
- Model: `product.unspsc.code`
- Type: inferred from arch
- Inherits: `product_unspsc.view_product_unspsc_code_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `code`, `l10n_mx_edi_hazardous_material`
- XPath or positional patches: 0

### `view_product_uom_categ_tree_unspsc_l10n_mx_edi_stock`
- Name: view.uom.categ.unspsc.list.l10n_mx_edi_stock
- Model: `product.unspsc.code`
- Type: inferred from arch
- Inherits: `product_unspsc.view_product_uom_categ_tree_unspsc`
- Root tag: `field`
- Field references: 2
- Sample fields: `code`, `l10n_mx_edi_hazardous_material`
- XPath or positional patches: 0

### `product_template_l10n_mx_hazardous`
- Name: product.template.form.l10n_mx_hazardous
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product_unspsc.product_template_unspsc`
- Root tag: `field`
- Field references: 5
- Sample fields: `l10n_mx_edi_hazard_package_type`, `l10n_mx_edi_hazardous_material_code_id`, `l10n_mx_edi_material_description`, `l10n_mx_edi_material_type`, `unspsc_code_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi_stock/Views]]

<!-- GENERATED:VIEWFILE -->
