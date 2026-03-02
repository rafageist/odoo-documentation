<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/l10n_latam_check_view.xml

- Module: [[docs/Community Addons/l10n_latam_check/l10n_latam_check|l10n_latam_check]]
- Scope: Community Addons
- Source file: `views/l10n_latam_check_view.xml`
- Views: 8
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `view_account_third_party_check_tree`
- Name: account.check.list
- Model: `l10n_latam.check`
- Type: inferred from arch
- Inherits: `view_account_own_check_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `current_journal_id`, `issue_state`, `original_journal_id`
- Buttons: `%(action_view_l10n_latam_payment_mass_transfer)d`
- XPath or positional patches: 1

### `view_account_own_check_tree`
- Name: account.check.list
- Model: `l10n_latam.check`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `amount`, `company_id`, `currency_id`, `issue_state`, `name`, `original_journal_id`, `partner_id`, `payment_date`, `payment_method_line_id`
- XPath or positional patches: 0

### `l10n_latam_check_view_form`
- Name: l10n_latam_check.view.form
- Model: `l10n_latam.check`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `amount`, `bank_id`, `company_id`, `currency_id`, `current_journal_id`, `issue_state`, `issuer_vat`, `name`, `original_journal_id`, `outstanding_line_id`, and 1 more
- Buttons: `action_show_journal_entry`, `action_show_reconciled_move`, `action_void`, `button_open_check_operations`, `button_open_payment`
- XPath or positional patches: 0

### `view_account_check_pivot`
- Name: account.check.calendar
- Model: `l10n_latam.check`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `amount`, `payment_date`
- XPath or positional patches: 0

### `view_account_check_calendar`
- Name: account.check.calendar
- Model: `l10n_latam.check`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 1
- Sample fields: `amount`
- XPath or positional patches: 0

### `view_account_third_party_check_operations_tree`
- Name: account.check.operations.list
- Model: `account.payment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `date`, `journal_id`, `name`, `partner_id`, `payment_type`, `state`
- XPath or positional patches: 0

### `view_account_payment_third_party_checks_search`
- Name: account.check.search
- Model: `l10n_latam.check`
- Type: inferred from arch
- Inherits: `view_account_payment_search`
- Root tag: `filter`
- Field references: 4
- Sample fields: `bank_id`, `current_journal_id`, `issuer_vat`, `original_journal_id`
- XPath or positional patches: 4

### `view_account_payment_search`
- Name: account.check.search
- Model: `l10n_latam.check`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `company_id`, `name`, `original_journal_id`, `partner_id`
- XPath or positional patches: 0

## Actions

- `action_third_party_check`: `act_window` Third Party Checks
- `action_own_check`: `act_window` Own Checks

## Menus

- `menu_third_party_check`: unnamed
- `menu_own_check`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/l10n_latam_check/Views]]

<!-- GENERATED:VIEWFILE -->
