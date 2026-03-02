<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/crm_activity_report_views.xml

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Source file: `report/crm_activity_report_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `crm_activity_report_view_search`
- Name: crm.activity.report.search
- Model: `crm.activity.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `author_id`, `lead_id`, `mail_activity_type_id`, `tag_ids`, `team_id`, `user_id`
- XPath or positional patches: 0

### `crm_activity_report_view_tree`
- Name: crm.activity.report.list
- Model: `crm.activity.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `author_id`, `body`, `company_id`, `date`, `mail_activity_type_id`, `tag_ids`
- XPath or positional patches: 0

### `crm_activity_report_view_pivot`
- Name: crm.activity.report.pivot
- Model: `crm.activity.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `date`, `mail_activity_type_id`
- XPath or positional patches: 0

### `crm_activity_report_view_graph`
- Name: crm.activity.report.graph
- Model: `crm.activity.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date`, `mail_activity_type_id`
- XPath or positional patches: 0

## Actions

- `crm_activity_report_action_team`: `act_window` Pipeline Activities
- `crm_activity_report_action`: `act_window` Activities

## Navigation

- **Parent:** [[docs/Community Addons/crm/Views]]

<!-- GENERATED:VIEWFILE -->
