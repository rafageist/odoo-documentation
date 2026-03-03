<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_tax_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_tax_views.xml`
- Views: 11
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_tax_group_form`
- Name: account.tax.group.form
- Model: `account.tax.group`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `advance_tax_payment_account_id`, `company_id`, `country_id`, `name`, `pos_receipt_label`, `preceding_subtotal`, `sequence`, `tax_payable_account_id`, `tax_receivable_account_id`
- XPath or positional patches: 0

### `view_tax_group_tree`
- Name: account.tax.group.list
- Model: `account.tax.group`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `advance_tax_payment_account_id`, `company_id`, `country_code`, `country_id`, `name`, `preceding_subtotal`, `sequence`, `tax_payable_account_id`, `tax_receivable_account_id`
- XPath or positional patches: 0

### `account_tax_group_view_search`
- Name: account.tax.group.search.filters
- Model: `account.tax.group`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `country_id`, `name`
- XPath or positional patches: 0

### `view_tax_form`
- Name: account.tax.form
- Model: `account.tax`
- Type: inferred from arch
- Root tag: `form`
- Field references: 28
- Sample fields: `active`, `amount`, `amount_type`, `analytic`, `cash_basis_transition_account_id`, `children_tax_ids`, `company_id`, `country_code`, `country_id`, `description`, and 18 more
- XPath or positional patches: 0

### `account_tax_view_search`
- Name: account.tax.search.filters
- Model: `account.tax`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `company_id`, `name`
- XPath or positional patches: 0

### `view_account_tax_search`
- Name: account.tax.search
- Model: `account.tax`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `company_id`, `description`, `fiscal_position_ids`, `name`
- XPath or positional patches: 0

### `view_tax_kanban`
- Name: account.tax.kanban
- Model: `account.tax`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `description`, `name`, `tax_scope`, `type_tax_use`
- XPath or positional patches: 0

### `account_tax_view_tree`
- Name: account.invoice.line.tax.search
- Model: `account.tax`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `description`, `display_name`, `tax_scope`
- XPath or positional patches: 0

### `tax_repartition_line_tree`
- Name: account.tax.repartition.line.list
- Model: `account.tax.repartition.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `account_id`, `company_id`, `factor_percent`, `repartition_type`, `sequence`, `tag_ids`, `tag_ids_domain`, `use_in_tax_closing`
- XPath or positional patches: 0

### `view_onboarding_tax_tree`
- Name: account.onboarding.tax.list
- Model: `account.tax`
- Type: inferred from arch
- Inherits: `account.view_tax_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_tax_tree`
- Name: account.tax.list
- Model: `account.tax`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `active`, `company_id`, `country_id`, `description`, `invoice_label`, `name`, `original_tax_ids`, `sequence`, `tax_scope`, `type_tax_use`
- XPath or positional patches: 0

## Actions

- `action_tax_group`: `act_window` Tax Groups
- `action_tax_form`: `act_window` Taxes

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
