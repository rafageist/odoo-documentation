<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/loyalty_program_views.xml

- Module: [[docs/Community Addons/loyalty/loyalty|loyalty]]
- Scope: Community Addons
- Source file: `views/loyalty_program_views.xml`
- Views: 4
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `loyalty_program_gift_ewallet_view_form`
- Name: loyalty.program.gift.ewallet.view.form
- Model: `loyalty.program`
- Type: inferred from arch
- Inherits: `loyalty_program_view_form`
- Root tag: `form`
- Field references: 1
- Sample fields: `program_type`
- XPath or positional patches: 1

### `loyalty_program_view_search`
- Name: loyalty.program.view.search
- Model: `loyalty.program`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `loyalty_program_view_tree`
- Name: loyalty.program.view.list
- Model: `loyalty.program`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `coupon_count_display`, `name`, `program_type`, `sequence`
- XPath or positional patches: 0

### `loyalty_program_view_form`
- Name: loyalty.program.view.form
- Model: `loyalty.program`
- Type: inferred from arch
- Root tag: `form`
- Field references: 24
- Sample fields: `active`, `applies_on`, `available_on`, `communication_plan_ids`, `company_id`, `coupon_count`, `currency_id`, `currency_symbol`, `date_from`, `date_to`, and 14 more
- Buttons: `%(loyalty_generate_wizard_action)d`, `action_open_loyalty_cards`
- XPath or positional patches: 0

## Actions

- `action_loyalty_program_form_gift_card_ewallet`: `view`
- `action_loyalty_program_tree_gift_card_ewallet`: `view`
- `loyalty_program_gift_ewallet_action`: `act_window` Gift cards & eWallet
- `action_loyalty_program_form_discount_loyalty`: `view`
- `action_loyalty_program_tree_discount_loyalty`: `view`
- `loyalty_program_discount_loyalty_action`: `act_window` Discount & Loyalty

## Navigation

- **Parent:** [[docs/Community Addons/loyalty/Views]]

<!-- GENERATED:VIEWFILE -->
