---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_social_insurance_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_social_insurance_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_social_insurance_view_form`
- Name: l10n.ch.social.insurance.view.form
- Model: `l10n.ch.social.insurance`
- Type: inferred from arch
- Root tag: `form`
- Field references: 27
- Sample fields: `ac_line_ids`, `admin_fees`, `age_start`, `age_stop_female`, `age_stop_male`, `amount`, `avs_line_ids`, `company_id`, `date_from`, `date_to`, and 17 more
- XPath or positional patches: 0

### `l10n_ch_social_insurance_view_tree`
- Name: l10n.ch.social.insurance.view.list
- Model: `l10n.ch.social.insurance`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `member_number`, `member_subnumber`, `name`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_social_insurance`: `act_window` AVS/AC Insurances

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

