<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/transfer_model_views.xml

- Module: [[docs/Enterprise Addons/account_transfer/account_transfer|account_transfer]]
- Scope: Enterprise Addons
- Source file: `views/transfer_model_views.xml`
- Views: 4
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `view_transfer_model_search`
- Name: account.auto.transfer.model.search
- Model: `account.transfer.model`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_transfer_model_form`
- Name: account.auto.transfer.model.form
- Model: `account.transfer.model`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `account_id`, `account_ids`, `conditions`, `date_start`, `date_stop`, `frequency`, `journal_id`, `line_ids`, `move_ids_count`, `name`, and 2 more
- Buttons: `%(generated_transfers_action)d`, `action_disable`, `action_enable`, `action_perform_auto_transfer`
- XPath or positional patches: 0

### `view_transfer_model_tree`
- Name: account.auto.transfer.model.list
- Model: `account.transfer.model`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `date_start`, `date_stop`, `frequency`, `name`
- XPath or positional patches: 0

### `view_generated_transfer_search`
- Name: account.auto.transfer.search
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_move_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `transfer_model_id`
- XPath or positional patches: 1

## Actions

- `generated_transfers_action`: `act_window` Generated Entries
- `transfer_model_action`: `act_window` Transfers

## Menus

- `menu_auto_transfer`: Transfers

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_transfer/Views]]

<!-- GENERATED:VIEWFILE -->
