<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/calendar_popover_delete_wizard.xml

- Module: [[docs/Community Addons/calendar/calendar|calendar]]
- Scope: Community Addons
- Source file: `wizard/calendar_popover_delete_wizard.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_event_delete_wizard_form`
- Name: calendar.popover.delete.wizard.form
- Model: `calendar.popover.delete.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `body`, `calendar_event_id`, `recipient_ids`, `subject`
- Buttons: `action_delete`, `action_send_mail_and_delete`
- XPath or positional patches: 0

### `calendar_popover_delete_view`
- Name: calendar.popover.delete.wizard.view.form
- Model: `calendar.popover.delete.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `delete`
- Buttons: `close`
- XPath or positional patches: 0

## Actions

- `action_event_delete_wizard`: `act_window` Event Cancel Wizard

## Navigation

- **Parent:** [[docs/Community Addons/calendar/Views]]

<!-- GENERATED:VIEWFILE -->
