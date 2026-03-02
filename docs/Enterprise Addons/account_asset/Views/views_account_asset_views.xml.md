<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_asset_views.xml

- Module: [[docs/Enterprise Addons/account_asset/account_asset|account_asset]]
- Scope: Enterprise Addons
- Source file: `views/account_asset_views.xml`
- Views: 7
- Actions: 5
- Menus: 3
- Rules: 0

## View records

### `view_move_line_tree_asset`
- Name: account.move.line.list.asset
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 6
- Sample fields: `amount_currency`, `analytic_distribution`, `balance`, `credit`, `debit`, `matching_number`
- XPath or positional patches: 0

### `view_account_asset_model_search`
- Name: account.asset.model.search
- Model: `account.asset`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_account_asset_search`
- Name: account.asset.search
- Model: `account.asset`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `acquisition_date`, `asset_properties`, `model_id`, `name`
- XPath or positional patches: 0

### `view_account_asset_model_tree`
- Name: account.asset.model.list
- Model: `account.asset`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `account_asset_id`, `account_depreciation_expense_id`, `account_depreciation_id`, `company_id`, `method`, `method_number`, `method_period`, `name`, `state`
- XPath or positional patches: 0

### `view_account_asset_tree`
- Name: account.asset.list
- Model: `account.asset`
- Type: inferred from arch
- Root tag: `list`
- Field references: 17
- Sample fields: `account_asset_id`, `account_depreciation_expense_id`, `account_depreciation_id`, `acquisition_date`, `activity_exception_decoration`, `activity_ids`, `analytic_distribution`, `asset_properties`, `book_value`, `company_id`, and 7 more
- XPath or positional patches: 0

### `view_account_asset_kanban`
- Name: account.asset.kanban
- Model: `account.asset`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `acquisition_date`, `currency_id`, `method_number`, `method_period`, `model_id`, `name`, `original_value`, `state`
- XPath or positional patches: 0

### `view_account_asset_form`
- Name: account.asset.form
- Model: `account.asset`
- Type: inferred from arch
- Root tag: `form`
- Field references: 47
- Sample fields: `account_asset_id`, `account_depreciation_expense_id`, `account_depreciation_id`, `account_id`, `account_type`, `acquisition_date`, `active`, `already_depreciated_amount_import`, `analytic_distribution`, `asset_depreciated_value`, and 37 more
- Buttons: `action_asset_modify`, `action_open_linked_assets`, `action_save_model`, `compute_depreciation_board`, `open_entries`, `open_increase`, `open_parent_id`, `resume_after_pause`, `set_to_cancelled`, `set_to_draft`, and 2 more
- XPath or positional patches: 0

## Actions

- `action_server_download_asset_template`: `server` Download Asset Import Template
- `action_account_asset_compute_depreciations`: `server` Compute Depreciation
- `action_account_asset_run`: `server` Confirm
- `action_account_asset_model_form`: `act_window` Asset Models
- `action_account_asset_form`: `act_window` Assets

## Menus

- `menu_finance_config_assets`: Assets and Revenues
- `menu_action_account_asset_model_form`: unnamed
- `menu_action_account_asset_form`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_asset/Views]]

<!-- GENERATED:VIEWFILE -->
