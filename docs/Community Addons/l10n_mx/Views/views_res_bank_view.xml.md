<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_bank_view.xml

- Module: [[docs/Community Addons/l10n_mx/l10n_mx|l10n_mx]]
- Scope: Community Addons
- Source file: `views/res_bank_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_partner_bank_tree_l10n_mx_edi_bank`
- Name: view.partner.bank.list.mx.inherit
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `base.view_partner_bank_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_mx_edi_clabe`
- XPath or positional patches: 1

### `view_partner_bank_form_l10n_mx_edi_bank`
- Name: view.partner.bank.form.mx.inherit
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `base.view_partner_bank_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `fiscal_country_codes`, `l10n_mx_edi_clabe`
- XPath or positional patches: 1

### `view_res_bank_inherit_l10n_mx_edi_bank`
- Name: view.res.bank.inherit.l10n_mx_edi_bank
- Model: `res.bank`
- Type: inferred from arch
- Inherits: `base.view_res_bank_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `fiscal_country_codes`, `l10n_mx_edi_code`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_mx/Views]]

<!-- GENERATED:VIEWFILE -->
