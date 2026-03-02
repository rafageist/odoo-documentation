<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_lead_rule_views.xml

- Module: [[docs/Community Addons/event_crm/event_crm|event_crm]]
- Scope: Community Addons
- Source file: `views/event_lead_rule_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `event_lead_rule_view_form`
- Name: event.lead.rule.view.form
- Model: `event.lead.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `active`, `company_id`, `event_id`, `event_registration_filter`, `event_type_ids`, `lead_creation_basis`, `lead_creation_trigger`, `lead_sales_team_id`, `lead_tag_ids`, `lead_type`, and 2 more
- Buttons: `action_execute_rule`
- XPath or positional patches: 0

### `event_lead_rule_view_tree`
- Name: event.lead.rule.view.list
- Model: `event.lead.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `event_id`, `event_type_ids`, `lead_creation_basis`, `lead_creation_trigger`, `name`
- XPath or positional patches: 0

### `event_lead_rule_view_search`
- Name: event.lead.rule.view.search
- Model: `event.lead.rule`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `event_lead_rule_answer_action`: `act_window` Event lead Rule
- `event_lead_rule_action`: `act_window` Lead Generation Rule

## Menus

- `event_lead_rule_menu`: Lead Generation

## Navigation

- **Parent:** [[docs/Community Addons/event_crm/Views]]

<!-- GENERATED:VIEWFILE -->
