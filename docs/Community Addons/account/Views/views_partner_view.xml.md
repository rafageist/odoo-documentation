<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/partner_view.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/partner_view.xml`
- Views: 8
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `partner_missing_account_list_view`
- Name: res.partner.list
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `res_partner_view_search`
- Name: res.partner.search.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `fiscal_country_codes`
- XPath or positional patches: 1

### `res_partner_view_tree`
- Name: res.partner.list.inherit.account
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `invoice_edi_format`, `invoice_sending_method`
- XPath or positional patches: 1

### `view_partner_property_form`
- Name: res.partner.property.form.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `xpath`
- Field references: 20
- Sample fields: `autopost_bills`, `bank_ids`, `credit`, `credit_limit`, `days_sales_outstanding`, `duplicate_bank_partner_ids`, `fiscal_country_codes`, `ignore_abnormal_invoice_amount`, `ignore_abnormal_invoice_date`, `invoice_edi_format`, and 10 more
- Buttons: `open_commercial_entity`
- XPath or positional patches: 6

### `partner_view_buttons`
- Name: partner.view.buttons
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `div`
- Field references: 7
- Sample fields: `company_registry`, `currency_id`, `partner_company_registry_placeholder`, `partner_vat_placeholder`, `supplier_invoice_count`, `total_invoiced`, `vat`
- Buttons: `%(account.res_partner_action_supplier_bills)d`, `action_view_partner_invoices`
- XPath or positional patches: 1

### `view_account_position_tree`
- Name: account.fiscal.position.list
- Model: `account.fiscal.position`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `name`, `sequence`
- XPath or positional patches: 0

### `view_account_position_filter`
- Name: account.fiscal.position.filter
- Model: `account.fiscal.position`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_account_position_form`
- Name: account.fiscal.position.form
- Model: `account.fiscal.position`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `account_dest_id`, `account_ids`, `account_src_id`, `active`, `auto_apply`, `company_country_id`, `company_id`, `country_group_id`, `country_id`, `fiscal_country_codes`, and 9 more
- Buttons: `action_create_foreign_taxes`, `action_open_related_taxes`
- XPath or positional patches: 0

## Actions

- `res_partner_action_supplier`: `act_window` Vendors
- `res_partner_action_customer`: `act_window` Customers
- `action_account_fiscal_position_form`: `act_window` Fiscal Positions
- `res_partner_action_supplier_bills`: `act_window` Vendor Bills

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
