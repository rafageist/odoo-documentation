<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/l10n_br/l10n_br|l10n_br]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `br_partner_tax_fields_form`
- Name: res.partner.form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `l10n_br_ie_code`, `l10n_br_im_code`, `l10n_br_isuf_code`
- XPath or positional patches: 1

### `br_partner_address_form`
- Name: partner.form.address.extended
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `city`, `city_id`, `country_enforce_cities`, `country_id`, `parent_id`, `state_id`, `street`, `street2`, `street_name`, `street_number`, and 3 more
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/l10n_br/Views]]

<!-- GENERATED:VIEWFILE -->
