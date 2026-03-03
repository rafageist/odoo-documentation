---
tags: [odoo, community, generated, views]
---

# wizard/privacy_lookup_wizard_views.xml

- Module: [[docs/Community Addons/privacy_lookup/privacy_lookup|privacy_lookup]]
- Scope: Community Addons
- Source file: `wizard/privacy_lookup_wizard_views.xml`
- Views: 3
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `privacy_lookup_wizard_line_view_search`
- Name: privacy.lookup.wizard.line.view.search
- Model: `privacy.lookup.wizard.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `has_active`, `is_active`, `res_model_id`
- XPath or positional patches: 0

### `privacy_lookup_wizard_line_view_tree`
- Name: privacy.lookup.wizard.line.view.list
- Model: `privacy.lookup.wizard.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `execution_details`, `has_active`, `is_active`, `is_unlinked`, `res_id`, `res_model`, `res_model_id`, `res_name`, `resource_ref`
- Buttons: `action_open_record`, `action_unlink`
- XPath or positional patches: 0

### `privacy_lookup_wizard_view_form`
- Name: privacy.lookup.wizard.view.form
- Model: `privacy.lookup.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `email`, `execution_details`, `line_count`, `line_ids`, `log_id`, `name`, `records_description`
- Buttons: `action_lookup`, `action_open_lines`
- XPath or positional patches: 0

## Actions

- `ir_action_server_action_privacy_lookup_user`: `server` Privacy Lookup
- `ir_action_server_action_privacy_lookup_partner`: `server` Privacy Lookup
- `action_privacy_lookup_wizard_line`: `act_window` Privacy Lookup Line
- `action_privacy_lookup_wizard`: `act_window` Privacy Lookup

## Navigation

- **Parent:** [[docs/Community Addons/privacy_lookup/Views]]

