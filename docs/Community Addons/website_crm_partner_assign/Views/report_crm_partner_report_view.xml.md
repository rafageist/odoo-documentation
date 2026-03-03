---
tags: [odoo, community, generated, views]
---

# report/crm_partner_report_view.xml

- Module: [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]
- Scope: Community Addons
- Source file: `report/crm_partner_report_view.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_report_crm_partner_assign_graph`
- Name: crm.partner.assign.report.graph
- Model: `crm.partner.report.assign`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `grade_id`, `nbr_opportunities`, `turnover`
- XPath or positional patches: 0

### `view_report_crm_partner_assign_filter`
- Name: crm.partner.report.assign.select
- Model: `crm.partner.report.assign`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `activation`, `grade_id`, `user_id`
- XPath or positional patches: 0

## Actions

- `action_report_crm_partner_assign`: `act_window` Partnership Analysis

## Menus

- `menu_report_crm_partner_assign_tree`: Partnerships

## Navigation

- **Parent:** [[docs/Community Addons/website_crm_partner_assign/Views]]

