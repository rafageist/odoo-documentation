<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/l10n_it_view.xml

- Module: [[docs/Community Addons/l10n_it_edi/l10n_it_edi|l10n_it_edi]]
- Scope: Community Addons
- Source file: `views/l10n_it_view.xml`
- Views: 8
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_it_ddt_list_view`
- Name: l10n_it.ddt.list.view
- Model: `l10n_it.ddt`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `date`, `name`
- XPath or positional patches: 0

### `l10n_it_ddt`
- Name: ddt.form.l10n.it
- Model: `l10n_it.ddt`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `date`, `name`
- XPath or positional patches: 0

### `account_invoice_form_l10n_it`
- Name: account.move.form.l10n.it
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `data`
- Field references: 17
- Sample fields: `l10n_it_cig`, `l10n_it_cup`, `l10n_it_ddt_id`, `l10n_it_document_type`, `l10n_it_edi_attachment_file`, `l10n_it_edi_attachment_name`, `l10n_it_edi_button_label`, `l10n_it_edi_header`, `l10n_it_edi_is_self_invoice`, `l10n_it_edi_state`, and 7 more
- Buttons: `action_check_l10n_it_edi`, `action_l10n_it_edi_send`
- XPath or positional patches: 6

### `view_account_invoice_filter`
- Name: account.invoice.select.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `l10n_it_edi_attachment_name`, `l10n_it_edi_state`, `l10n_it_edi_transaction`
- XPath or positional patches: 1

### `view_invoice_tree_inherit`
- Name: account.move.list.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `l10n_it_edi_attachment_name`, `l10n_it_edi_state`, `l10n_it_edi_transaction`, `status_in_payment`
- XPath or positional patches: 0

### `res_company_form_l10n_it`
- Name: res.company.form.l10n.it
- Model: `res.company`
- Type: inferred from arch
- Inherits: `base.view_company_form`
- Root tag: `data`
- Field references: 10
- Sample fields: `l10n_it_codice_fiscale`, `l10n_it_eco_index_liquidation_state`, `l10n_it_eco_index_number`, `l10n_it_eco_index_office`, `l10n_it_eco_index_share_capital`, `l10n_it_eco_index_sole_shareholder`, `l10n_it_has_eco_index`, `l10n_it_has_tax_representative`, `l10n_it_tax_representative_partner_id`, `l10n_it_tax_system`
- XPath or positional patches: 2

### `res_partner_form_l10n_it`
- Name: res.partner.form.l10n.it
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `data`
- Field references: 3
- Sample fields: `l10n_it_codice_fiscale`, `l10n_it_pa_index`, `l10n_it_pec_email`
- XPath or positional patches: 1

### `res_partner_tree_l10n_it`
- Name: res.partner.list.l10n.it
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `l10n_it_codice_fiscale`, `l10n_it_pa_index`
- XPath or positional patches: 1

## Actions

- `action_ddt_account`: `act_window` Transport Document

## Menus

- `menu_action_ddt_account`: DDT

## Navigation

- **Parent:** [[docs/Community Addons/l10n_it_edi/Views]]

<!-- GENERATED:VIEWFILE -->
