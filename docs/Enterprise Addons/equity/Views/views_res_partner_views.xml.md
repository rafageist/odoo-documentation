---
tags: [odoo, enterprise, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Enterprise Addons/equity/equity|equity]]
- Scope: Enterprise Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `equity_dashboard_res_partner`
- Name: equity.dashboard.res.partner
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `equity_currency_id`, `equity_kanban_dashboard_graph`, `equity_last_valuation`, `equity_shareholders_count`, `equity_transaction_count`, `name`
- XPath or positional patches: 0

### `equity_view_partner_form`
- Name: equity.view.partner.form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `div`
- Field references: 17
- Sample fields: `auth_rep_role`, `control_method`, `end_date`, `equity_formation_date`, `equity_legal_form`, `equity_shareholders_count`, `holder_id`, `ownership`, `partner_id`, `start_date`, and 7 more
- Buttons: `equity.action_equity_cap_table`
- XPath or positional patches: 2

## Actions

- `action_equity_dashboard_res_partner`: `server` Equity
- `action_equity_ubo_report`: `report` Print UBO
- `action_equity_request_ubo_form`: `act_window` Request UBO Form

## Navigation

- **Parent:** [[docs/Enterprise Addons/equity/Views]]

