<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_swissdec_job_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_swissdec_job_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_l10n_ch_swissdec_job_result_status_form`
- Name: l10n.ch.swissdec.job.status.form
- Model: `l10n.ch.swissdec.job.result`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `status_response_json`
- XPath or positional patches: 0

### `view_l10n_ch_swissdec_job_result_form`
- Name: l10n.ch.swissdec.job.result.form
- Model: `l10n.ch.swissdec.job.result`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `completion_url`, `credential_key`, `credential_password`, `declaration_id`, `dialog_message_ids`, `dialog_response_json`, `domain`, `has_lpp_contributions`, `has_proof_of_insurance`, `has_st_corrections`, and 11 more
- Buttons: `action_get_dialog`, `action_get_result_from_declare_salary`, `action_open_proof_of_insurance`, `action_poll`, `action_reply_dialog`, `generate_is_statement`, `generate_proof_of_insurance`, `import_lpp_contributions`, `import_source_tax_corrections`
- XPath or positional patches: 2

### `view_l10n_ch_swissdec_job_result_tree`
- Name: l10n.ch.swissdec.job.result.tree
- Model: `l10n.ch.swissdec.job.result`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `display_name`, `general_state`, `result_state`, `status_response_json`, `success_state`
- Buttons: `action_open_completion_url`, `action_open_status_notification`, `action_open_swissdec_job_result`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
