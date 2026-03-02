<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/delivery_carrier_views.xml

- Module: [[docs/Community Addons/delivery/delivery|delivery]]
- Scope: Community Addons
- Source file: `views/delivery_carrier_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_delivery_carrier_form`
- Name: delivery.carrier.form
- Model: `delivery.carrier`
- Type: inferred from arch
- Root tag: `form`
- Field references: 30
- Sample fields: `active`, `allow_cash_on_delivery`, `amount`, `carrier_description`, `company_id`, `country_ids`, `currency_id`, `debug_logging`, `delivery_type`, `excluded_tag_ids`, and 20 more
- Buttons: `install_more_provider`, `toggle_debug`, `toggle_prod_environment`
- XPath or positional patches: 0

### `view_delivery_carrier_search`
- Name: delivery.carrier.search
- Model: `delivery.carrier`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `delivery_type`, `name`
- XPath or positional patches: 0

### `view_delivery_carrier_tree`
- Name: delivery.carrier.list
- Model: `delivery.carrier`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `country_ids`, `delivery_type`, `excluded_tag_ids`, `max_volume`, `max_weight`, `must_have_tag_ids`, `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `action_delivery_carrier_form`: `act_window` Delivery Methods

## Menus

- `sale_menu_action_delivery_carrier_form`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/delivery/Views]]

<!-- GENERATED:VIEWFILE -->
