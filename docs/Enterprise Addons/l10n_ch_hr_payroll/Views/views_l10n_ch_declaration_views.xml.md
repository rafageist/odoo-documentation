<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_declaration_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_declaration_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_swissdec_declaration_tree`
- Name: l10n.ch.swissdec.declaration.tree
- Model: `l10n.ch.swissdec.declaration`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `swissdec_declaration_id`, `transmission_date`
- XPath or positional patches: 0

### `l10n_ch_swissdec_declaration_form`
- Name: l10n.ch.swissdec.declaration.form
- Model: `l10n.ch.swissdec.declaration`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `credential_key`, `credential_password`, `display_name`, `general_state`, `general_warnings`, `l10n_ch_swissdec_job_result_ids`, `name`, `result_response_json`, `result_state`, `state`, and 5 more
- Buttons: `action_get_dialog_and_open_result`, `action_get_result_from_declare_salary`, `action_open_completion_url`, `action_open_status_notification`, `action_open_swissdec_job_result`, `get_status_from_declare_salary`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
