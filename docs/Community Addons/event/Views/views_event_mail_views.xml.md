<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_mail_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_mail_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_event_mail_tree`
- Name: event.mail.list
- Model: `event.mail`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `event_id`, `mail_count_done`, `mail_state`, `scheduled_date`, `template_ref`
- XPath or positional patches: 0

### `view_event_mail_form`
- Name: event.mail.form
- Model: `event.mail`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `event_id`, `interval_nbr`, `interval_type`, `interval_unit`, `mail_registration_ids`, `mail_sent`, `mail_state`, `registration_id`, `scheduled_date`, `template_ref`
- XPath or positional patches: 0

## Actions

- `action_event_mail`: `act_window` Events Mail Schedulers

## Menus

- `menu_event_mail_schedulers`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
