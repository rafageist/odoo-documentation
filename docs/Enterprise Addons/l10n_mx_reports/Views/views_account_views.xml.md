<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_reports/l10n_mx_reports|l10n_mx_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_list`
- Name: account.account.list.inherit.l10n_mx_reports
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_list`
- Root tag: `field`
- Field references: 2
- Sample fields: `code`, `l10n_mx_is_sat_invalid`
- XPath or positional patches: 0

### `view_account_form_l10n_mx_reports`
- Name: account.account.form.inherit.l10n_mx_reports
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_mx_is_sat_invalid`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_reports/Views]]

<!-- GENERATED:VIEWFILE -->
