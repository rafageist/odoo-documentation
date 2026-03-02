<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/quality_views.xml

- Module: [[docs/Enterprise Addons/quality_control_worksheet/quality_control_worksheet|quality_control_worksheet]]
- Scope: Enterprise Addons
- Source file: `views/quality_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `quality_point_view_form_inherit_quality_control_worksheet`
- Name: quality.point.view.form.inherit.quality.worksheet
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality.quality_point_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `worksheet_model_name`, `worksheet_success_conditions`, `worksheet_template_id`
- XPath or positional patches: 1

### `quality_check_view_form_inherit_worksheet`
- Name: quality.check.view.form.inherit.worksheet
- Model: `quality.check`
- Type: inferred from arch
- Inherits: `quality_control.quality_check_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `worksheet_count`, `worksheet_template_id`
- Buttons: `action_open_quality_check_wizard`, `action_worksheet_check`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_control_worksheet/Views]]

<!-- GENERATED:VIEWFILE -->
