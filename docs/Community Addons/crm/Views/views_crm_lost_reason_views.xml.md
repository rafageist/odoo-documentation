<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_lost_reason_views.xml

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Source file: `views/crm_lost_reason_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `crm_lost_reason_view_tree`
- Name: crm.lost.reason.list
- Model: `crm.lost.reason`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `crm_lost_reason_view_form`
- Name: crm.lost.reason.form
- Model: `crm.lost.reason`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `active`, `leads_count`, `name`
- Buttons: `action_lost_leads`
- XPath or positional patches: 0

### `crm_lost_reason_view_search`
- Name: crm.lost.reason.view.search
- Model: `crm.lost.reason`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `crm_lost_reason_action`: `act_window` Lost Reasons

## Navigation

- **Parent:** [[docs/Community Addons/crm/Views]]

<!-- GENERATED:VIEWFILE -->
