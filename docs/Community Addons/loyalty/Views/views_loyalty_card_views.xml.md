<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/loyalty_card_views.xml

- Module: [[docs/Community Addons/loyalty/loyalty|loyalty]]
- Scope: Community Addons
- Source file: `views/loyalty_card_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `loyalty_card_view_search`
- Name: loyalty.card.view.search
- Model: `loyalty.card`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `code`, `partner_id`, `program_id`
- XPath or positional patches: 0

### `loyalty_card_view_tree`
- Name: loyalty.card.view.list
- Model: `loyalty.card`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `code`, `create_date`, `expiration_date`, `partner_id`, `points_display`, `program_id`
- Buttons: `action_coupon_send`
- XPath or positional patches: 0

### `loyalty_card_view_form`
- Name: loyalty.card.view.form
- Model: `loyalty.card`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `code`, `create_date`, `description`, `expiration_date`, `history_ids`, `issued`, `order_id`, `partner_id`, `points_display`, `used`
- Buttons: `action_loyalty_update_balance`
- XPath or positional patches: 0

## Actions

- `loyalty_card_action`: `act_window` Coupons

## Navigation

- **Parent:** [[docs/Community Addons/loyalty/Views]]

<!-- GENERATED:VIEWFILE -->
