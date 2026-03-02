<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_users.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/res_users.xml`
- Views: 6
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_users_view_form`
- Name: res.users.form.inherit
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 10
- Sample fields: `email_domain_placeholder`, `employee_count`, `employee_id`, `employee_ids`, `mobile_phone`, `pin`, `share`, `work_email`, `work_location_id`, `work_phone`
- Buttons: `action_create_employee`, `action_open_employees`, `action_related_contact`
- XPath or positional patches: 7

### `view_users_simple_form`
- Name: view.users.simple.form.hr
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_simple_form`
- Root tag: `sheet`
- Field references: 0
- XPath or positional patches: 1

### `view_users_simple_form_inherit_hr`
- Name: view.users.simple.form.inherit.hr
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_simple_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `create_employee`, `create_employee_id`, `employee_count`
- Buttons: `action_open_employees`
- XPath or positional patches: 2

### `res_users_view_form_preferences`
- Name: res.users.preferences.form.inherit
- Model: `res.users`
- Type: inferred from arch
- Inherits: `res_users_view_form_simple_modif`
- Root tag: `form`
- Field references: 16
- Sample fields: `emergency_contact`, `emergency_phone`, `employee_ids`, `mobile_phone`, `pin`, `private_city`, `private_country_id`, `private_email`, `private_phone`, `private_state_id`, and 6 more
- XPath or positional patches: 8

### `view_users_form_simple_modif_resource`
- Name: res.users.preferences.form.resource
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `field`
- Field references: 2
- Sample fields: `is_system`, `tz`
- XPath or positional patches: 1

### `res_users_view_form_simple_modif`
- Name: res.users.preferences.form.simplified.inherit
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `form`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `res_users_action_my`: `act_window` Change my Preferences

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
