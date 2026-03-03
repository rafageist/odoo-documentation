---
tags: [odoo, community, generated, views]
---

# views/res_partner_view.xml

- Module: [[docs/Community Addons/l10n_my_edi/l10n_my_edi|l10n_my_edi]]
- Scope: Community Addons
- Source file: `views/res_partner_view.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_partner_form_inherit_l10n_my_myinvois`
- Name: res.partner.form.inherit.l10n_my_myinvois
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `group`
- Field references: 7
- Sample fields: `l10n_my_edi_display_tin_warning`, `l10n_my_edi_industrial_classification`, `l10n_my_edi_malaysian_tin`, `l10n_my_identification_number`, `l10n_my_identification_number_placeholder`, `l10n_my_identification_type`, `l10n_my_tin_validation_state`
- Buttons: `action_validate_tin`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_my_edi/Views]]

