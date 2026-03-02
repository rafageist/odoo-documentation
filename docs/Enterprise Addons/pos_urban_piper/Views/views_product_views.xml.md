<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/pos_urban_piper/pos_urban_piper|pos_urban_piper]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_template_search_view_inherit_pos_urban_piper`
- Name: product.template.search.view.inherit.pos.urban.piper
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `product_template_tree_view_pos_urban_piper`
- Name: product.template.product.list.inherit.pos.urban.piper
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `field`
- Field references: 3
- Sample fields: `available_in_pos`, `urbanpiper_meal_type`, `urbanpiper_pos_config_ids`
- XPath or positional patches: 0

### `product_template_only_form_view_inherit_pos_urban_piper`
- Name: product.template.view.form.inherit.pos_urban_piper
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `is_alcoholic_on_urbanpiper`, `is_recommended_on_urbanpiper`, `urbanpiper_meal_type`, `urbanpiper_pos_config_ids`, `urbanpiper_pos_platform_ids`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_urban_piper/Views]]

<!-- GENERATED:VIEWFILE -->
