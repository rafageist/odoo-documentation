<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_au_super_stream_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/l10n_au_super_stream_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_au_super_stream_line_view_tree`
- Name: l10n_au.super.stream.line.view.list
- Model: `l10n_au.super.stream.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `amount_total`, `employer_id`, `name`, `payee_id`, `payslip_id`, `proportion`
- XPath or positional patches: 0

### `l10n_au_super_stream_line_view_form`
- Name: l10n_au.super.stream.line.view.form
- Model: `l10n_au.super.stream.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `allowed_super_account_ids`, `award_or_productivity_amount`, `child_contributions_amount`, `employee_id`, `employer_id`, `end_date`, `name`, `other_third_party_contributions_amount`, `payee_id`, `payslip_id`, and 9 more
- XPath or positional patches: 0

### `l10n_au_super_stream_view_tree`
- Name: l10n_au.super.stream.view.list
- Model: `l10n_au.super.stream`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `activity_date_deadline`, `activity_ids`, `company_id`, `display_name`
- XPath or positional patches: 0

### `l10n_au_super_stream_view_form`
- Name: l10n_au.super.stream.view.form
- Model: `l10n_au.super.stream`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `company_id`, `currency_id`, `display_name`, `file_version`, `journal_id`, `l10n_au_super_stream_lines`, `payment_id`, `source_entity_id`, `source_entity_id_type`, `state`, and 1 more
- Buttons: `action_confirm`, `action_draft`, `action_open_payment`, `action_register_super_payment`
- XPath or positional patches: 0

## Actions

- `l10n_au_super_stream_action`: `act_window` Super Contributions

## Menus

- `l10n_au_super_stream`: Super Contributions

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Views]]

<!-- GENERATED:VIEWFILE -->
