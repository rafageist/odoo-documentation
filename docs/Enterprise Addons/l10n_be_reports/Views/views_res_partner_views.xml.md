---
tags: [odoo, enterprise, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_reports/l10n_be_reports|l10n_be_reports]]
- Scope: Enterprise Addons
- Source file: `views/res_partner_views.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_partner_view_search`
- Name: res.partner.search.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `res_partner_vat_listing_warning_view_tree`
- Name: res.partner.vat.listing.warning.view.list
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `country_id`, `name`, `vat`
- XPath or positional patches: 0

### `res_partner_view_form_281_50_required_field`
- Name: res.partner.view.form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `l10n_be_reports.res_partner_view_form_inherit`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 6

### `view_partner_281_50_required_fields`
- Name: res.partner.list
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `citizen_identification`, `city`, `country_id`, `is_company`, `name`, `phone`, `street`, `vat`, `zip`
- XPath or positional patches: 0

### `res_partner_view_form_inherit_mail`
- Name: res.partner.view.form.inherit.mail
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `mail.res_partner_view_form_inherit_mail`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `res_partner_view_form`
- Name: res.partner.view.form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_reports/Views]]

