<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/delivery_carrier_views.xml

- Module: [[docs/Enterprise Addons/delivery_envia/delivery_envia|delivery_envia]]
- Scope: Enterprise Addons
- Source file: `views/delivery_carrier_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_package_type_form_inherit_envia`
- Name: stock.package.type.forms.inherit.envia
- Model: `stock.package.type`
- Type: inferred from arch
- Inherits: `stock.stock_package_type_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `envia_mail_type`, `shipper_package_code`
- XPath or positional patches: 1

### `view_delivery_carrier_form_inherit_delivery_envia`
- Name: delivery.carrier.form.inherit.delivery.envia
- Model: `delivery.carrier`
- Type: inferred from arch
- Inherits: `delivery.view_delivery_carrier_form`
- Root tag: `xpath`
- Field references: 13
- Sample fields: `country_id`, `envia_currency_id`, `envia_default_package_type_id`, `envia_label_file_type`, `envia_label_stock_type`, `envia_lift_delivery`, `envia_lift_pickup`, `envia_production_api_key`, `envia_residential_delivery`, `envia_residential_pickup`, and 3 more
- Buttons: `action_open_envia_wizard`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_envia/Views]]

<!-- GENERATED:VIEWFILE -->
