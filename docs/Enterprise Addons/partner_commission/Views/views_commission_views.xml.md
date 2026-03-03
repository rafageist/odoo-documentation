---
tags: [odoo, enterprise, generated, views]
---

# views/commission_views.xml

- Module: [[docs/Enterprise Addons/partner_commission/partner_commission|partner_commission]]
- Scope: Enterprise Addons
- Source file: `views/commission_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `commission_rule_tree_view`
- Name: commission.rule.list.view
- Model: `commission.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `category_id`, `is_capped`, `max_commission`, `pricelist_id`, `product_id`, `rate`, `template_id`
- XPath or positional patches: 0

### `commission_plan_search_view`
- Name: commission.plan.search.view
- Model: `commission.plan`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `company_id`, `name`
- XPath or positional patches: 0

### `commission_plan_tree_view`
- Name: commission.plan.list.view
- Model: `commission.plan`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `product_id`
- XPath or positional patches: 0

### `commission_plan_form_view`
- Name: commission.plan.form.view
- Model: `commission.plan`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `commission_rule_ids`, `company_id`, `name`, `product_id`
- XPath or positional patches: 0

## Actions

- `action_commission_plans`: `act_window` Commission Plans

## Menus

- `menu_commission_plans`: Commission Plans

## Navigation

- **Parent:** [[docs/Enterprise Addons/partner_commission/Views]]

