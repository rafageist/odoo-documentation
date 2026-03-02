<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_iap_lead_mining_request_views.xml

- Module: [[docs/Community Addons/crm_iap_mine/crm_iap_mine|crm_iap_mine]]
- Scope: Community Addons
- Source file: `views/crm_iap_lead_mining_request_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `crm_iap_lead_mining_request_view_search`
- Name: crm.iap.lead.mining.request.view.search
- Model: `crm.iap.lead.mining.request`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `country_ids`, `industry_ids`, `name`, `tag_ids`, `team_id`, `user_id`
- XPath or positional patches: 0

### `crm_iap_lead_mining_request_view_tree`
- Name: crm.iap.lead.mining.request.view.list
- Model: `crm.iap.lead.mining.request`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `country_ids`, `industry_ids`, `lead_number`, `name`, `search_type`, `state`, `tag_ids`, `team_id`, `user_id`
- XPath or positional patches: 0

### `crm_iap_lead_mining_request_view_form`
- Name: crm.iap.lead.mining.request.view.form
- Model: `crm.iap.lead.mining.request`
- Type: inferred from arch
- Root tag: `form`
- Field references: 22
- Sample fields: `available_state_ids`, `company_size_max`, `company_size_min`, `contact_filter_type`, `contact_number`, `country_ids`, `error_type`, `filter_on_size`, `industry_ids`, `lead_count`, and 12 more
- Buttons: `action_buy_credits`, `action_get_lead_action`, `action_get_opportunity_action`, `action_submit`
- XPath or positional patches: 0

## Actions

- `crm_iap_lead_mining_request_action`: `act_window` Lead Mining Requests

## Navigation

- **Parent:** [[docs/Community Addons/crm_iap_mine/Views]]

<!-- GENERATED:VIEWFILE -->
