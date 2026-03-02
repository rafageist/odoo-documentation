<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_event_views.xml

- Module: [[docs/Community Addons/event_crm/event_crm|event_crm]]
- Scope: Community Addons
- Source file: `views/event_event_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_view_tree`
- Name: event.event.list.inherit.event.crm
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `lead_count`
- XPath or positional patches: 1

### `event_view_form`
- Name: event.event.form.inherit.event.crm
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `lead_count`
- Buttons: `%(crm_lead_action_from_event)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/event_crm/Views]]

<!-- GENERATED:VIEWFILE -->
