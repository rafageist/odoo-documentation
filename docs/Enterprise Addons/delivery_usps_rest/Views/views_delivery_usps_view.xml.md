---
tags: [odoo, enterprise, generated, views]
---

# views/delivery_usps_view.xml

- Module: [[docs/Enterprise Addons/delivery_usps_rest/delivery_usps_rest|delivery_usps_rest]]
- Scope: Enterprise Addons
- Source file: `views/delivery_usps_view.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_delivery_carrier_form_with_provider_usps`
- Name: delivery.carrier.form.provider.usps
- Model: `delivery.carrier`
- Type: inferred from arch
- Inherits: `delivery.view_delivery_carrier_form`
- Root tag: `xpath`
- Field references: 20
- Sample fields: `get_return_label_from_portal`, `return_label_on_delivery`, `usps_api_key`, `usps_api_secret`, `usps_crid`, `usps_default_package_type_id`, `usps_delivery_nature`, `usps_domestic_rating_indicator`, `usps_domestic_service`, `usps_eps_account_number`, and 10 more
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_usps_rest/Views]]

