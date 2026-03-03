<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/setup_wizards_view.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `wizard/setup_wizards_view.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `init_accounts_tree`
- Name: account.setup.opening.move.line.list
- Model: `account.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `account_type`, `active`, `code`, `company_ids`, `name`, `opening_balance`, `opening_credit`, `opening_debit`, `reconcile`, `tag_ids`, and 1 more
- XPath or positional patches: 0

### `setup_credit_card_account_wizard`
- Name: account.online.sync.res.partner.credit.card.setup.form
- Model: `account.setup.bank.manual.config`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `acc_number`, `bank_id`, `linked_journal_id`
- Buttons: `validate`
- XPath or positional patches: 0

### `setup_bank_account_wizard`
- Name: account.online.sync.res.partner.bank.setup.form
- Model: `account.setup.bank.manual.config`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `acc_number`, `bank_bic`, `bank_id`, `linked_journal_id`
- Buttons: `validate`
- XPath or positional patches: 0

### `setup_financial_year_opening_form`
- Name: account.financial.year.op.setup.wizard.form
- Model: `account.financial.year.op`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `fiscalyear_last_day`, `fiscalyear_last_month`, `opening_date`, `opening_move_posted`
- Buttons: `action_save_onboarding_fiscal_year`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
