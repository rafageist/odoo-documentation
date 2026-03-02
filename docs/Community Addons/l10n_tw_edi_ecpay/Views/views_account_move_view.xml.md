<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Community Addons/l10n_tw_edi_ecpay/l10n_tw_edi_ecpay|l10n_tw_edi_ecpay]]
- Scope: Community Addons
- Source file: `views/account_move_view.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_move_form_inherit_ecpay`
- Name: ecpay_invoice_view_form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 15
- Sample fields: `l10n_tw_edi_allowance_notify_way`, `l10n_tw_edi_carrier_number`, `l10n_tw_edi_carrier_number_2`, `l10n_tw_edi_carrier_type`, `l10n_tw_edi_clearance_mark`, `l10n_tw_edi_ecpay_invoice_id`, `l10n_tw_edi_invalidate_reason`, `l10n_tw_edi_invoice_create_date`, `l10n_tw_edi_is_print`, `l10n_tw_edi_love_code`, and 5 more
- XPath or positional patches: 1

## Actions

- `action_print_ecpay_invoice`: `server` Print Ecpay invoice

## Navigation

- **Parent:** [[docs/Community Addons/l10n_tw_edi_ecpay/Views]]

<!-- GENERATED:VIEWFILE -->
