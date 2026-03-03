---
tags: [odoo, community, generated, views]
---

# wizard/project_share_wizard_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `wizard/project_share_wizard_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `project_share_wizard_confirm_form`
- Name: project.share.wizard.view.form
- Model: `project.share.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 0
- Buttons: `action_send_mail`
- XPath or positional patches: 0

### `project_share_wizard_view_form`
- Name: project.share.wizard.view.form
- Model: `project.share.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `access_mode`, `collaborator_ids`, `partner_id`, `res_id`, `res_model`, `send_invitation`, `share_link`
- Buttons: `action_share_record`
- XPath or positional patches: 0

## Actions

- `project_share_wizard_action`: `act_window` Share Project

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

