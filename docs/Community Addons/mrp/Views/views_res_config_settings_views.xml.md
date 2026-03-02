<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.mrp
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 10
- Sample fields: `group_mrp_byproducts`, `group_mrp_reception_report`, `group_mrp_routings`, `group_mrp_workorder_dependencies`, `group_unlocked_by_default`, `module_mrp_mps`, `module_mrp_subcontracting`, `module_quality_control`, `module_quality_control_worksheet`, `module_stock_barcode`
- Buttons: `%(mrp.mrp_workcenter_action)d`
- XPath or positional patches: 1

## Actions

- `action_mrp_configuration`: `act_window` Settings

## Menus

- `menu_mrp_config`: Settings

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

<!-- GENERATED:VIEWFILE -->
