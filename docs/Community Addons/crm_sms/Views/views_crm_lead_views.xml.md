<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Community Addons/crm_sms/crm_sms|crm_sms]]
- Scope: Community Addons
- Source file: `views/crm_lead_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `crm_lead_view_tree_opportunity_reporting`
- Name: crm.lead.list.opportunity.reporting.inherit.sms
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_tree_opportunity_reporting`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `crm_case_tree_view_oppor`
- Name: crm.lead.list.opportunity.inherit.sms
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_oppor`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(crm_sms.crm_lead_act_window_sms_composer_multi)d`, `%(crm_sms.crm_lead_act_window_sms_composer_single)d`
- XPath or positional patches: 2

## Actions

- `crm_lead_act_window_sms_composer_multi`: `act_window` Send SMS
- `crm_lead_act_window_sms_composer_single`: `act_window` Send SMS

## Navigation

- **Parent:** [[docs/Community Addons/crm_sms/Views]]

<!-- GENERATED:VIEWFILE -->
