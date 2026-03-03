---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_au_stp_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_api/l10n_au_hr_payroll_api|l10n_au_hr_payroll_api]]
- Scope: Enterprise Addons
- Source file: `views/l10n_au_stp_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_au_stp_view_list`
- Name: l10n_au.stp.tree
- Model: `l10n_au.stp`
- Type: inferred from arch
- Inherits: `l10n_au_hr_payroll_account.l10n_au_stp_view_tree`
- Root tag: `list`
- Field references: 1
- Sample fields: `ato_status`
- XPath or positional patches: 1

### `l10n_au_stp_view_form`
- Name: l10n_au.stp.form
- Model: `l10n_au.stp`
- Type: inferred from arch
- Inherits: `l10n_au_hr_payroll_account.l10n_au_stp_form_wizard`
- Root tag: `button`
- Field references: 0
- Buttons: `action_draft`, `action_pre_submit`, `action_replace_file`, `l10n_au_hr_payroll_account.l10n_au_action_submit_stp`, `update_status`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_api/Views]]

