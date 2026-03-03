---
tags: [odoo, enterprise, generated, views]
---

# wizard/helpdesk_stage_delete_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `wizard/helpdesk_stage_delete_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_helpdesk_stage_unarchive_wizard`
- Name: helpdesk.stage.delete.wizard.form
- Model: `helpdesk.stage.delete.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 0
- Buttons: `action_unarchive_ticket`
- XPath or positional patches: 0

### `view_helpdesk_stage_delete_confirmation_wizard`
- Name: helpdesk.stage.delete.wizard.form
- Model: `helpdesk.stage.delete.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `name`, `team_ids`
- Buttons: `action_confirm`
- XPath or positional patches: 0

### `view_helpdesk_stage_delete_wizard`
- Name: helpdesk.stage.delete.wizard.form
- Model: `helpdesk.stage.delete.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `stages_active`, `ticket_count`
- Buttons: `action_archive`, `action_unlink`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

