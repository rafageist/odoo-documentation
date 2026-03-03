---
tags: [odoo, community, generated, views]
---

# wizard/sms_composer_views.xml

- Module: [[docs/Community Addons/sms/sms|sms]]
- Scope: Community Addons
- Source file: `wizard/sms_composer_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `sms_composer_view_form`
- Name: sms.composer.view.form
- Model: `sms.composer`
- Type: inferred from arch
- Root tag: `form`
- Field references: 20
- Sample fields: `body`, `comment_single_recipient`, `composition_mode`, `mass_force_send`, `mass_keep_log`, `number_field_name`, `numbers`, `recipient_invalid_count`, `recipient_single_description`, `recipient_single_number`, and 10 more
- Buttons: `action_send_sms`, `action_send_sms_mass_now`
- XPath or positional patches: 0

## Actions

- `sms_composer_action_form`: `act_window` Send SMS

## Navigation

- **Parent:** [[docs/Community Addons/sms/Views]]

