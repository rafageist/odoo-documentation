<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_team_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/crm_team_views.xml`
- Views: 2
- Actions: 5
- Menus: 0
- Rules: 0

## View records

### `crm_team_view_kanban_dashboard`
- Name: crm.team.view.kanban.dashboard.inherit.sale
- Model: `crm.team`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_view_kanban_dashboard`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `invoiced_target`
- XPath or positional patches: 3

### `crm_team_salesteams_view_form`
- Name: crm.team.form
- Model: `crm.team`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `company_id`, `invoiced_target`
- XPath or positional patches: 0

## Actions

- `sales_team.mail_activity_type_action_config_sales`: `act_window`
- `action_orders_to_invoice_salesteams`: `act_window` Sales Orders
- `action_orders_salesteams`: `act_window` Sales Orders
- `action_quotation_form`: `act_window` New Quotation
- `action_quotations_salesteams`: `act_window` Quotations

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

<!-- GENERATED:VIEWFILE -->
