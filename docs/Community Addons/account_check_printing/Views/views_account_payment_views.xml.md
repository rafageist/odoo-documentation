<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_payment_views.xml

- Module: [[docs/Community Addons/account_check_printing/account_check_printing|account_check_printing]]
- Scope: Community Addons
- Source file: `views/account_payment_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_payment_check_printing_search`
- Name: account.payment.check.printing.search
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_account_payment_form_inherited`
- Name: account.payment.form.inherited
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `check_amount_in_words`, `check_manual_sequencing`, `check_number`, `show_check_number`
- Buttons: `action_void_check`, `print_checks`, `unmark_as_sent`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/account_check_printing/Views]]

<!-- GENERATED:VIEWFILE -->
