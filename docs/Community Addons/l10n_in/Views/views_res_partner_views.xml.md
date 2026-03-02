<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/l10n_in/l10n_in|l10n_in]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_in_view_partner_base_vat_form`
- Name: l10n.in.gstin.status.view.partner.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base_vat.view_partner_base_vat_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_in_gstin_verified_date`
- Buttons: `action_l10n_in_verify_gstin_status`
- XPath or positional patches: 1

### `l10n_in_view_res_partner_filter`
- Name: l10n.in.view.res.partner.filter.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_in_pan_entity_id`, `user_id`
- XPath or positional patches: 1

### `l10n_in_view_partner_tree`
- Name: l10n.in.res.partner.tree
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_in_pan_entity_id`
- XPath or positional patches: 1

### `l10n_in_view_partner_form`
- Name: l10n.in.res.partner.vat.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `l10n_in_gst_state_warning`, `l10n_in_gst_treatment`, `l10n_in_pan_entity_id`, `l10n_in_tan`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/l10n_in/Views]]

<!-- GENERATED:VIEWFILE -->
