---
tags: [odoo, community, generated, views]
---

# views/sms_template_views.xml

- Module: [[docs/Community Addons/sms/sms|sms]]
- Scope: Community Addons
- Source file: `views/sms_template_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `sms_template_view_search`
- Name: sms.template.view.search
- Model: `sms.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `model_id`, `name`
- XPath or positional patches: 0

### `sms_template_view_tree`
- Name: sms.template.view.list
- Model: `sms.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `model_id`, `name`
- XPath or positional patches: 0

### `sms_template_view_form`
- Name: sms.template.view.form
- Model: `sms.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `body`, `lang`, `model`, `model_id`, `name`, `sidebar_action_id`, `template_fs`
- Buttons: `%(sms_template_preview_action)d`, `%(sms_template_reset_action)d`, `action_create_sidebar_action`, `action_unlink_sidebar_action`
- XPath or positional patches: 0

## Actions

- `sms_template_action`: `act_window` Templates

## Menus

- `sms_template_menu`: SMS Templates

## Navigation

- **Parent:** [[docs/Community Addons/sms/Views]]

