<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_template_view_search_sale_timesheet`
- Name: product.template.search.timesheet
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_product_timesheet_form`
- Name: product.template.timesheet.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `sale.product_template_form_view`
- Root tag: `field`
- Field references: 3
- Sample fields: `product_tooltip`, `service_upsell_threshold`, `service_upsell_threshold_ratio`
- XPath or positional patches: 0

## Actions

- `product_template_action_default_services`: `act_window` Services

## Navigation

- **Parent:** [[docs/Community Addons/sale_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
