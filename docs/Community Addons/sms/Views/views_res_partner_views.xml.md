<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/sms/sms|sms]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `res_partner_view_form`
- Name: res.partner.view.form.inherit.sms
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `phone_blacklisted`, `phone_sanitized`
- Buttons: `phone_action_blacklist_remove`
- XPath or positional patches: 2

## Actions

- `res_partner_act_window_sms_composer_single`: `act_window` Send SMS
- `res_partner_act_window_sms_composer_multi`: `act_window` Send SMS

## Navigation

- **Parent:** [[docs/Community Addons/sms/Views]]

<!-- GENERATED:VIEWFILE -->
