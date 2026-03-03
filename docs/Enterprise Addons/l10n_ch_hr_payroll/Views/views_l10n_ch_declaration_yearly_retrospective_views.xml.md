---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_declaration_yearly_retrospective_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_declaration_yearly_retrospective_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_insurance_report_view_transmission_form`
- Name: ch.yearly.report.form
- Model: `ch.yearly.report`
- Type: inferred from arch
- Inherits: `l10n_ch_hr_payroll.l10n_ch_swissdec_transmitter_form`
- Root tag: `header`
- Field references: 10
- Sample fields: `avs_institution_ids`, `caf_institution_ids`, `ijm_institution_ids`, `incomplete_declaration`, `laa_institution_ids`, `laac_institution_ids`, `substituted_declaration_id`, `tax_certificates`, `tax_cross_border_institutions`, `wage_statement_count`
- Buttons: `action_open_wage_statements`, `create_eiv_file`, `generate_ahv_report`, `generate_fak_report`, `generate_free_ahv_report`, `generate_ktg_report`, `generate_laa_report`, `generate_laac_report`, `generate_tax_accounting_reports`, `generate_txb_report`, and 1 more
- XPath or positional patches: 3

## Actions

- `l10n_ch_yearly_retrospective_action`: `act_window` Yearly Salary Declaration

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

