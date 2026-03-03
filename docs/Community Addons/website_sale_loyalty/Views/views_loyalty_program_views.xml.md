---
tags: [odoo, community, generated, views]
---

# views/loyalty_program_views.xml

- Module: [[docs/Community Addons/website_sale_loyalty/website_sale_loyalty|website_sale_loyalty]]
- Scope: Community Addons
- Source file: `views/loyalty_program_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `loyalty_program_view_tree_inherit_website_sale_loyalty`
- Name: loyalty.program.view.list.inherit.website.sale.loyalty
- Model: `loyalty.program`
- Type: inferred from arch
- Inherits: `loyalty.loyalty_program_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `company_id`, `coupon_count_display`, `website_id`
- Buttons: `action_program_share`
- XPath or positional patches: 0

### `loyalty_program_view_form_inherit_website_sale_loyalty`
- Name: loyalty.program.view.form.inherit.website.sale.loyalty
- Model: `loyalty.program`
- Type: inferred from arch
- Inherits: `sale_loyalty.loyalty_program_view_form_inherit_sale_loyalty`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `ecommerce_ok`, `website_id`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Community Addons/website_sale_loyalty/Views]]

