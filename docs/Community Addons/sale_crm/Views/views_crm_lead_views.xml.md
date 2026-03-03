---
tags: [odoo, community, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Community Addons/sale_crm/sale_crm|sale_crm]]
- Scope: Community Addons
- Source file: `views/crm_lead_views.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `crm_case_form_view_oppor`
- Name: crm.lead.oppor.inherited.crm
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `quotation_count`, `sale_amount_total`, `sale_order_count`
- Buttons: `action_sale_quotations_new`, `action_schedule_meeting`, `action_set_won_rainbowman`, `action_view_sale_order`, `action_view_sale_quotation`
- XPath or positional patches: 1

## Actions

- `sales_team.mail_activity_type_action_config_sales`: `act_window`
- `crm.crm_lead_opportunities`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/sale_crm/Views]]

