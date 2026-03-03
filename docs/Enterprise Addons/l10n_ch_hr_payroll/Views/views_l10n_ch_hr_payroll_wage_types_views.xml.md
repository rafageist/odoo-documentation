---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_hr_payroll_wage_types_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_hr_payroll_wage_types_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `swissdec_wage_types_form`
- Name: hr.salary.rule.view.form.l10n.ch.wage.types
- Model: `hr.salary.rule`
- Type: inferred from arch
- Inherits: `l10n_ch_hr_payroll_salary_rule`
- Root tag: `page`
- Field references: 17
- Sample fields: `l10n_ch_13th_month_hourly_included`, `l10n_ch_13th_month_included`, `l10n_ch_aanp_included`, `l10n_ch_ac_included`, `l10n_ch_caf_statement`, `l10n_ch_gross_included`, `l10n_ch_ijm_included`, `l10n_ch_is_periodic`, `l10n_ch_laac_included`, `l10n_ch_lpp_factor`, and 7 more
- XPath or positional patches: 2

### `l10n_ch_wage_type_search_view`
- Name: wage.type.search.view
- Model: `hr.salary.rule`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `code`, `l10n_ch_code`, `name`
- XPath or positional patches: 0

### `l10n_ch_hr_payroll_salary_rule_tree`
- Name: hr.salary.rule.view.tree.l10n.ch.wage.types
- Model: `hr.salary.rule`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_salary_rule_list`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_ch_code`, `name`
- XPath or positional patches: 0

### `l10n_ch_hr_payroll_salary_rule`
- Name: hr.salary.rule.view.form.l10n.ch.wage.types
- Model: `hr.salary.rule`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_salary_rule_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `code`, `l10n_ch_code`
- XPath or positional patches: 0

### `swissdec_wage_types_tree`
- Name: hr.salary.rule.view.tree.l10n.ch.wage.types
- Model: `hr.salary.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 19
- Sample fields: `category_id`, `code`, `l10n_ch_13th_month_hourly_included`, `l10n_ch_13th_month_included`, `l10n_ch_aanp_included`, `l10n_ch_ac_included`, `l10n_ch_code`, `l10n_ch_gross_included`, `l10n_ch_ijm_included`, `l10n_ch_laac_included`, and 9 more
- XPath or positional patches: 0

## Actions

- `l10n_ch_hr_payroll.action_hr_salary_rule_l10n_ch_wage_types`: `act_window` Wage Types

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

