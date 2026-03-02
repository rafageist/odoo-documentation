<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi_extended/l10n_mx_edi_extended|l10n_mx_edi_extended]]
- Scope: Enterprise Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_mx_edi_inh_res_partner_form`
- Name: res.partner.form.inherit.l10n_mx_edi
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `group`
- Field references: 2
- Sample fields: `l10n_mx_edi_curp`, `l10n_mx_edi_external_trade`
- XPath or positional patches: 2

### `mx_partner_address_form`
- Name: l10n_mx_edi.res.partner.address.form
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `city`, `city_id`, `country_enforce_cities`, `country_id`, `l10n_mx_edi_colony`, `l10n_mx_edi_colony_code`, `l10n_mx_edi_locality`, `l10n_mx_edi_locality_id`, `parent_id`, `state_id`, and 7 more
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi_extended/Views]]

<!-- GENERATED:VIEWFILE -->
