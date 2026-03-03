---
tags: [odoo, enterprise, generated, views]
---

# wizard/product_fetch_image_wizard_views.xml

- Module: [[docs/Enterprise Addons/product_barcodelookup/product_barcodelookup|product_barcodelookup]]
- Scope: Enterprise Addons
- Source file: `wizard/product_fetch_image_wizard_views.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `product_fetch_image_wizard_view_form`
- Name: product.fetch.image.wizard.view
- Model: `product.fetch.image.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `nb_products_selected`, `nb_products_to_process`, `nb_products_unable_to_process`
- Buttons: `action_fetch_image`
- XPath or positional patches: 0

## Actions

- `product_product_action_get_pic_with_barcode`: `act_window` Get Pictures from Barcode Lookup
- `product_template_action_get_pic_with_barcode`: `act_window` Get Pictures from Barcode Lookup

## Navigation

- **Parent:** [[docs/Enterprise Addons/product_barcodelookup/Views]]

