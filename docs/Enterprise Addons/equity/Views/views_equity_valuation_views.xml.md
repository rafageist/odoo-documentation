<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/equity_valuation_views.xml

- Module: [[docs/Enterprise Addons/equity/equity|equity]]
- Scope: Enterprise Addons
- Source file: `views/equity_valuation_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_equity_valuation_form`
- Name: equity.valuation.form
- Model: `equity.valuation`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `date`, `equity_currency_id`, `event`, `partner_id`, `share_price`, `shares`, `valuation`
- XPath or positional patches: 0

### `view_equity_valuation_list`
- Name: equity.valuation.list
- Model: `equity.valuation`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `attachment_number`, `date`, `equity_currency_id`, `event`, `partner_id`, `securities`, `security_price`, `share_price`, `shares`, `valuation`
- XPath or positional patches: 0

### `view_equity_valuation_search`
- Name: equity.valuation.search
- Model: `equity.valuation`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

## Actions

- `action_equity_valuation_form`: `act_window` Create Valuation
- `action_equity_valuation`: `act_window` Valuations

## Navigation

- **Parent:** [[docs/Enterprise Addons/equity/Views]]

<!-- GENERATED:VIEWFILE -->
