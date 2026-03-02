<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_au_super_stream_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_api/l10n_au_hr_payroll_api|l10n_au_hr_payroll_api]]
- Scope: Enterprise Addons
- Source file: `views/l10n_au_super_stream_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_au_super_stream_line_view_tree`
- Name: l10n_au.super.stream.line.view.list
- Model: `l10n_au.super.stream.line`
- Type: inferred from arch
- Inherits: `l10n_au_hr_payroll_account.l10n_au_super_stream_line_view_tree`
- Root tag: `list`
- Field references: 2
- Sample fields: `dest_payment_ref`, `dest_payment_status`
- XPath or positional patches: 1

### `l10n_au_super_stream_view_tree`
- Name: l10n_au.super.stream.view.list
- Model: `l10n_au.super.stream`
- Type: inferred from arch
- Inherits: `l10n_au_hr_payroll_account.l10n_au_super_stream_view_tree`
- Root tag: `list`
- Field references: 1
- Sample fields: `payment_status`
- XPath or positional patches: 1

### `l10n_au_super_stream_view_form`
- Name: l10n_au.super.stream.view.form
- Model: `l10n_au.super.stream`
- Type: inferred from arch
- Inherits: `l10n_au_hr_payroll_account.l10n_au_super_stream_view_form`
- Root tag: `header`
- Field references: 5
- Sample fields: `days_funds_update`, `message_id`, `payment_ref`, `source_payment_status`, `super_stream_file`
- Buttons: `action_cancel`, `action_resubmit_failed`, `action_update_funds`, `update_payment_status`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_api/Views]]

<!-- GENERATED:VIEWFILE -->
