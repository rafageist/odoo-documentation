---
tags: [odoo, enterprise, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Enterprise Addons/l10n_br_avatax/l10n_br_avatax|l10n_br_avatax]]
- Scope: Enterprise Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_partner_view_list`
- Name: res.partner.view.list
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `city_id`, `l10n_br_activity_sector`, `l10n_br_tax_regime`, `l10n_br_taxpayer`, `l10n_latam_identification_type_id`, `name`, `state_id`, `street2`, `street_name`, `street_number`, and 2 more
- Buttons: `l10n_br_action_open_res_partner`
- XPath or positional patches: 0

### `res_partner_view_form`
- Name: res.partner.view.form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `group`
- Field references: 7
- Sample fields: `l10n_br_activity_sector`, `l10n_br_is_subject_csll`, `l10n_br_iss_simples_rate`, `l10n_br_subject_cofins`, `l10n_br_subject_pis`, `l10n_br_tax_regime`, `l10n_br_taxpayer`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_br_avatax/Views]]

