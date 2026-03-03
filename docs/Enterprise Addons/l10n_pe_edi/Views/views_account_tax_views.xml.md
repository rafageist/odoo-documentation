---
tags: [odoo, enterprise, generated, views]
---

# views/account_tax_views.xml

- Module: [[docs/Enterprise Addons/l10n_pe_edi/l10n_pe_edi|l10n_pe_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_tax_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_tax_group_tree_inherit_l10n_pe_edi`
- Name: account.tax.group.list.inherit.l10n_pe_edi
- Model: `account.tax.group`
- Type: inferred from arch
- Inherits: `account.view_tax_group_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_pe_edi_code`
- XPath or positional patches: 1

### `account_tax_form_inherit_l10n_pe_edi`
- Name: account.tax.form.inherit.l10n_pe_edi
- Model: `account.tax`
- Type: inferred from arch
- Inherits: `l10n_pe.view_tax_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_pe_edi_affectation_reason`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_pe_edi/Views]]

