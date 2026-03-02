<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/privacy_log_views.xml

- Module: [[docs/Community Addons/privacy_lookup/privacy_lookup|privacy_lookup]]
- Scope: Community Addons
- Source file: `views/privacy_log_views.xml`
- Views: 2
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `privacy_log_view_form`
- Name: privacy.log.view.form
- Model: `privacy.log`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `additional_note`, `anonymized_email`, `anonymized_name`, `date`, `execution_details`, `records_description`, `user_id`
- XPath or positional patches: 0

### `privacy_log_view_list`
- Name: privacy.log.view.list
- Model: `privacy.log`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `anonymized_email`, `anonymized_name`, `date`, `execution_details`, `user_id`
- XPath or positional patches: 0

## Actions

- `privacy_log_form_action`: `act_window` Privacy Logs
- `privacy_log_action`: `act_window` Privacy Logs

## Menus

- `pricacy_log_menu`: Privacy Logs
- `privacy_menu`: Privacy

## Navigation

- **Parent:** [[docs/Community Addons/privacy_lookup/Views]]

<!-- GENERATED:VIEWFILE -->
