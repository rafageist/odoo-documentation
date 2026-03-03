---
tags: [odoo, community, generated, views]
---

# views/pos_payment_method_views.xml

- Module: [[docs/Community Addons/pos_mercado_pago/pos_mercado_pago|pos_mercado_pago]]
- Scope: Community Addons
- Source file: `views/pos_payment_method_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `pos_payment_method_view_form_inherit_pos_mercado_pago`
- Name: pos.payment.method.form.inherit.mercado_pago
- Model: `pos.payment.method`
- Type: inferred from arch
- Inherits: `point_of_sale.pos_payment_method_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `mp_bearer_token`, `mp_id_point_smart`, `mp_webhook_secret_key`
- Buttons: `force_pdv`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/pos_mercado_pago/Views]]

