---
tags: [odoo, enterprise, generated, views]
---

# views/pos_payment_method_views.xml

- Module: [[docs/Enterprise Addons/pos_tyro/pos_tyro|pos_tyro]]
- Scope: Enterprise Addons
- Source file: `views/pos_payment_method_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `pos_payment_method_view_form_inherit_pos_tyro`
- Name: pos.payment.method.form.inherit.tyro
- Model: `pos.payment.method`
- Type: inferred from arch
- Inherits: `point_of_sale.pos_payment_method_view_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `tyro_always_print_merchant_receipt`, `tyro_integrated_receipts`, `tyro_integration_key`, `tyro_merchant_id`, `tyro_mode`, `tyro_surcharge_product_id`, `tyro_terminal_id`
- Buttons: `action_get_tyro_report`, `action_pair_tyro_terminal`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_tyro/Views]]

