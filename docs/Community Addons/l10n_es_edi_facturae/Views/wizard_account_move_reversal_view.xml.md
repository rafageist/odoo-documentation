<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/account_move_reversal_view.xml

- Module: [[docs/Community Addons/l10n_es_edi_facturae/l10n_es_edi_facturae|l10n_es_edi_facturae]]
- Scope: Community Addons
- Source file: `wizard/account_move_reversal_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_move_reversal_inherit_l10n_es_edi_facturae`
- Name: account.move.reversal.form.inherit.l10n_es_edi_facturae
- Model: `account.move.reversal`
- Type: inferred from arch
- Inherits: `account.view_account_move_reversal`
- Root tag: `field`
- Field references: 3
- Sample fields: `country_code`, `l10n_es_edi_facturae_reason_code`, `reason`
- XPath or positional patches: 0

### `view_tax_tree_inherit_l10n_es_edi_facturae`
- Name: account.tax.list.inherit.l10n_es_edi_facturae
- Model: `account.tax`
- Type: inferred from arch
- Inherits: `account.view_tax_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `country_code`, `country_id`, `l10n_es_edi_facturae_tax_type`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/l10n_es_edi_facturae/Views]]

<!-- GENERATED:VIEWFILE -->
