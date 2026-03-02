<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_tax_views.xml

- Module: [[docs/Community Addons/l10n_ke/l10n_ke|l10n_ke]]
- Scope: Community Addons
- Source file: `views/account_tax_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_ke_inherit_view_tax_form`
- Name: l10n.ke.inherit.account.tax.form
- Model: `account.tax`
- Type: inferred from arch
- Inherits: `account.view_tax_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ke_item_code_id`
- XPath or positional patches: 1

### `l10n_ke_inherit_view_tax_tree`
- Name: l10n.ke.account.tax.list
- Model: `account.tax`
- Type: inferred from arch
- Inherits: `account.view_tax_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `description`, `l10n_ke_item_code_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ke/Views]]

<!-- GENERATED:VIEWFILE -->
