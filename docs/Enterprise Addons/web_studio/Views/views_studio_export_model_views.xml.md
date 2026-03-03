---
tags: [odoo, enterprise, generated, views]
---

# views/studio_export_model_views.xml

- Module: [[docs/Enterprise Addons/web_studio/web_studio|web_studio]]
- Scope: Enterprise Addons
- Source file: `views/studio_export_model_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `models_to_export_form_view`
- Name: models.to.export.form
- Model: `studio.export.model`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `domain`, `excluded_fields`, `field_description`, `include_attachment`, `is_demo_data`, `model_id`, `model_name`, `name`, `readonly`, `relation`, and 4 more
- XPath or positional patches: 0

### `models_to_export_list`
- Name: models.to.export.list
- Model: `studio.export.model`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `include_attachment`, `is_demo_data`, `model_id`, `records_count`, `sequence`, `updatable`
- Buttons: `action_preset`, `web_studio.action_studio_export_wizard`
- XPath or positional patches: 0

## Actions

- `action_models_to_export`: `act_window` Studio Export

## Menus

- `menu_models_to_export`: Studio Export

## Navigation

- **Parent:** [[docs/Enterprise Addons/web_studio/Views]]

