<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/delivery_carrier_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/delivery_carrier_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_delivery_carrier_search`
- Name: delivery.carrier.search.inherit
- Model: `delivery.carrier`
- Type: inferred from arch
- Inherits: `delivery.view_delivery_carrier_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_delivery_carrier_tree`
- Name: delivery.carrier.list.inherit
- Model: `delivery.carrier`
- Type: inferred from arch
- Inherits: `delivery.view_delivery_carrier_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `delivery_type`, `is_published`, `website_id`
- XPath or positional patches: 0

### `view_delivery_carrier_form_website_delivery`
- Name: delivery.carrier.website.form
- Model: `delivery.carrier`
- Type: inferred from arch
- Inherits: `delivery.view_delivery_carrier_form`
- Root tag: `field`
- Field references: 5
- Sample fields: `carrier_description`, `company_id`, `is_published`, `website_description`, `website_id`
- Buttons: `toggle_prod_environment`, `website_publish_button`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

<!-- GENERATED:VIEWFILE -->
