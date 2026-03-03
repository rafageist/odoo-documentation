---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/hr_recruitment_extract/hr_recruitment_extract|hr_recruitment_extract]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.hr.recruitment.extract
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `hr_recruitment.res_config_settings_view_form`
- Root tag: `setting`
- Field references: 1
- Sample fields: `recruitment_extract_show_ocr_option_selection`
- Buttons: `%(ir_module_module_action_open_job_board_modules)d`
- XPath or positional patches: 3

## Actions

- `ir_module_module_action_open_job_board_modules`: `act_window` Job Boards

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_extract/Views]]

