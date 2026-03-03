---
tags: [odoo, community, generated, views]
---

# views/onboarding_views.xml

- Module: [[docs/Community Addons/onboarding/onboarding|onboarding]]
- Scope: Community Addons
- Source file: `views/onboarding_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `onboarding_onboarding_step_view_form`
- Name: onboarding.onboarding.step.view.form
- Model: `onboarding.onboarding.step`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `button_text`, `current_step_state`, `description`, `done_icon`, `done_text`, `is_per_company`, `onboarding_ids`, `panel_step_open_action_name`, `step_image`, `step_image_alt`, and 2 more
- XPath or positional patches: 0

### `onboarding_onboarding_step_view_tree`
- Name: onboarding.onboarding.step.view.list
- Model: `onboarding.onboarding.step`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `current_step_state`, `is_per_company`, `onboarding_ids`, `sequence`, `title`
- XPath or positional patches: 0

### `onboarding_onboarding_view_form`
- Name: onboarding.onboarding.view.form
- Model: `onboarding.onboarding`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `current_progress_id`, `is_onboarding_closed`, `is_per_company`, `name`, `route_name`, `step_ids`
- Buttons: `action_toggle_visibility`
- XPath or positional patches: 0

### `onboarding_onboarding_view_tree`
- Name: onboarding.onboarding.view.list
- Model: `onboarding.onboarding`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `current_onboarding_state`, `is_onboarding_closed`, `is_per_company`, `name`, `sequence`
- Buttons: `action_toggle_visibility`
- XPath or positional patches: 0

## Actions

- `action_view_onboarding_step`: `act_window` Onboarding Steps
- `action_view_onboarding_onboarding`: `act_window` Onboardings

## Navigation

- **Parent:** [[docs/Community Addons/onboarding/Views]]

