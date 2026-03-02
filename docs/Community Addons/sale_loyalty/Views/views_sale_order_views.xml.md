<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/sale_loyalty/sale_loyalty|sale_loyalty]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_order_view_form_inherit_sale_loyalty`
- Name: sale.order.view.form.inherit.sale.loyalty
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `div`
- Field references: 3
- Sample fields: `gift_card_count`, `is_reward_line`, `loyalty_data`
- Buttons: `%(sale_loyalty.sale_loyalty_coupon_wizard_action)d`, `action_open_discount_wizard`, `action_open_reward_wizard`, `action_view_gift_cards`
- XPath or positional patches: 6

## Navigation

- **Parent:** [[docs/Community Addons/sale_loyalty/Views]]

<!-- GENERATED:VIEWFILE -->
