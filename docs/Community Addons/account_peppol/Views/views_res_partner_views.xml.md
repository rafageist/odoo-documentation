<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/account_peppol/account_peppol|account_peppol]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_partner_form_account_peppol`
- Name: res.partner.form.account.peppol
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `data`
- Field references: 5
- Sample fields: `available_peppol_edi_formats`, `available_peppol_sending_methods`, `bank_account_count`, `is_peppol_edi_format`, `peppol_verification_state`
- Buttons: `button_account_peppol_check_partner_endpoint`
- XPath or positional patches: 5

## Actions

- `partner_action_verify_peppol`: `server` Verify Peppol

## Navigation

- **Parent:** [[docs/Community Addons/account_peppol/Views]]

<!-- GENERATED:VIEWFILE -->
