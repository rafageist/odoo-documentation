<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_invoice_views.xml

- Module: [[docs/Community Addons/l10n_in/l10n_in|l10n_in]]
- Scope: Community Addons
- Source file: `views/account_invoice_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_line_list_l10n_in_withholding`
- Name: account.move.line.list.l10n.in.withholding
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `account_id`, `l10n_in_tds_tcs_section_id`, `name`, `price_total`, `product_id`, `tax_ids`
- XPath or positional patches: 0

### `invoice_form_inherit_l10n_in`
- Name: account.move.form.inherit.l10n.in
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 16
- Sample fields: `l10n_in_gst_treatment`, `l10n_in_gstin_verified_date`, `l10n_in_hsn_code`, `l10n_in_partner_gstin_status`, `l10n_in_reseller_partner_id`, `l10n_in_shipping_bill_date`, `l10n_in_shipping_bill_number`, `l10n_in_shipping_port_code_id`, `l10n_in_state_id`, `l10n_in_total_withholding_amount`, and 6 more
- Buttons: `%(l10n_in_withholding_entry_form_action)d`, `action_l10n_in_apply_higher_tax`, `action_l10n_in_withholding_entries`, `l10n_in_verify_partner_gstin_status`
- XPath or positional patches: 9

## Navigation

- **Parent:** [[docs/Community Addons/l10n_in/Views]]

<!-- GENERATED:VIEWFILE -->
