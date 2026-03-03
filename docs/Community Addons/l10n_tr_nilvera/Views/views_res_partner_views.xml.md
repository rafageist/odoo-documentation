---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/l10n_tr_nilvera/l10n_tr_nilvera|l10n_tr_nilvera]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_partner_property_form_inherit_ubl_tr`
- Name: res.partner.property.form.inherit.ubl.tr
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account_edi_ubl_cii.view_partner_property_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `l10n_tr_nilvera_customer_alias_id`, `l10n_tr_nilvera_customer_status`
- Buttons: `l10n_tr_check_nilvera_customer`
- XPath or positional patches: 1

## Actions

- `action_account_reports_customer_statements_do_followup`: `server` Verify Nilvera Status

## Navigation

- **Parent:** [[docs/Community Addons/l10n_tr_nilvera/Views]]

