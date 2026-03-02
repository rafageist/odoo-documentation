<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_view.xml

- Module: [[docs/Community Addons/l10n_ar/l10n_ar|l10n_ar]]
- Scope: Community Addons
- Source file: `views/res_partner_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_res_partner_filter`
- Name: view.res.partner.filter.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `category_id`, `l10n_ar_afip_responsibility_type_id`
- XPath or positional patches: 1

### `view_partner_property_form`
- Name: res.partner.form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `l10n_ar_gross_income_number`, `l10n_ar_gross_income_type`, `property_account_position_id`
- XPath or positional patches: 0

### `base_view_partner_form`
- Name: res.partner.form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `l10n_latam_base.view_partner_latam_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ar_afip_responsibility_type_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ar/Views]]

<!-- GENERATED:VIEWFILE -->
