---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_view.xml

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_view.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `res_config_settings_view_employee_form`
- Name: res.config.settings.view.form.inherit.hr.appraisal
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `hr.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `appraisal_plan`, `duration_after_recruitment`, `duration_first_appraisal`, `duration_next_appraisal`, `module_hr_appraisal_survey`
- XPath or positional patches: 1

## Actions

- `hr_appraisal_config_settings_action`: `act_window` Settings

## Menus

- `hr_appraisal_menu_configuration`: Settings

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Views]]

