<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_reveal_views.xml

- Module: [[docs/Community Addons/website_crm_iap_reveal/website_crm_iap_reveal|website_crm_iap_reveal]]
- Scope: Community Addons
- Source file: `views/crm_reveal_views.xml`
- Views: 5
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `crm_reveal_view_tree`
- Name: crm.reveal.view.list
- Model: `crm.reveal.view`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `create_date`, `reveal_ip`, `reveal_rule_id`, `reveal_state`
- XPath or positional patches: 0

### `crm_reveal_view_form`
- Name: crm.reveal.view.form
- Model: `crm.reveal.view`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `create_date`, `reveal_ip`, `reveal_rule_id`, `reveal_state`
- XPath or positional patches: 0

### `crm_reveal_rule_view_search`
- Name: crm.reveal.rule.view.search
- Model: `crm.reveal.rule`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `crm_reveal_rule_tree`
- Name: crm.reveal.rule.list
- Model: `crm.reveal.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `lead_type`, `name`, `sequence`
- XPath or positional patches: 0

### `crm_reveal_rule_form`
- Name: crm.reveal.rule.form
- Model: `crm.reveal.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 25
- Sample fields: `active`, `company_size_max`, `company_size_min`, `contact_filter_type`, `country_ids`, `extra_contacts`, `filter_on_size`, `industry_tag_ids`, `lead_count`, `lead_for`, and 15 more
- Buttons: `action_get_lead_tree_view`, `action_get_opportunity_tree_view`
- XPath or positional patches: 0

## Actions

- `crm_reveal_view_action`: `act_window` Lead Generation Views
- `crm_reveal_rule_action`: `act_window` Visits to Leads Rules

## Navigation

- **Parent:** [[docs/Community Addons/website_crm_iap_reveal/Views]]

<!-- GENERATED:VIEWFILE -->
