<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Community Addons/event_crm/event_crm|event_crm]]
- Scope: Community Addons
- Source file: `views/crm_lead_views.xml`
- Views: 1
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `crm_lead_view_form`
- Name: crm.lead.view.form.inherit.event.crm
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `registration_count`, `registration_ids`
- Buttons: `%(event_registration_action_from_lead)d`
- XPath or positional patches: 1

## Actions

- `crm_lead_action_from_event`: `act_window` Leads
- `crm_lead_action_from_registration`: `act_window` Leads
- `event_registration_action_from_lead`: `act_window` Event registrations

## Navigation

- **Parent:** [[docs/Community Addons/event_crm/Views]]

<!-- GENERATED:VIEWFILE -->
