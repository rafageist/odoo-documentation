<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/delivery_carrier_views.xml

- Module: [[docs/Enterprise Addons/delivery_easypost/delivery_easypost|delivery_easypost]]
- Scope: Enterprise Addons
- Source file: `views/delivery_carrier_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_package_type_form_inherit_easypost`
- Name: stock.package.type.forms.inherit.easypost
- Model: `stock.package.type`
- Type: inferred from arch
- Inherits: `stock.stock_package_type_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `easypost_carrier`, `length_uom_name`
- XPath or positional patches: 2

### `view_delivery_carrier_form_inherit_delivery_easypost`
- Name: delivery.carrier.form.inherit.delivery.easypost
- Model: `delivery.carrier`
- Type: inferred from arch
- Inherits: `delivery.view_delivery_carrier_form`
- Root tag: `page`
- Field references: 9
- Sample fields: `can_generate_return`, `easypost_default_package_type_id`, `easypost_default_service_id`, `easypost_delivery_type`, `easypost_label_file_type`, `easypost_production_api_key`, `easypost_test_api_key`, `get_return_label_from_portal`, `return_label_on_delivery`
- Buttons: `action_get_carrier_type`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_easypost/Views]]

<!-- GENERATED:VIEWFILE -->
