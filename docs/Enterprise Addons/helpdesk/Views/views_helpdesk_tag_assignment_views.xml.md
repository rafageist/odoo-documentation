---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_tag_assignment_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_tag_assignment_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_helpdesk_tag_assignment_search`
- Name: helpdesk.tag.assignment.search
- Model: `helpdesk.tag.assignment`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `tag_id`, `user_ids`
- XPath or positional patches: 0

### `view_helpdesk_tag_assignment_list`
- Name: helpdesk.tag.assignment.list
- Model: `helpdesk.tag.assignment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `tag_id`, `team_id`, `user_ids`
- XPath or positional patches: 0

## Actions

- `action_helpdesk_tag_assignment`: `act_window` Configure Tags Handled by Team Members

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

