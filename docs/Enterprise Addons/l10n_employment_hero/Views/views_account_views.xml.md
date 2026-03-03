---
tags: [odoo, enterprise, generated, views]
---

# views/account_views.xml

- Module: [[docs/Enterprise Addons/l10n_employment_hero/l10n_employment_hero|l10n_employment_hero]]
- Scope: Enterprise Addons
- Source file: `views/account_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_tax_form_inherit`
- Name: account.tax.form.inherit
- Model: `account.tax`
- Type: inferred from arch
- Inherits: `account.view_tax_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `active`, `employment_hero_enable`, `employment_hero_tax_identifier`
- XPath or positional patches: 0

### `view_account_form_inherit`
- Name: account.account.form.inherit
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `currency_id`, `employment_hero_account_identifier`, `employment_hero_enable`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_employment_hero/Views]]

