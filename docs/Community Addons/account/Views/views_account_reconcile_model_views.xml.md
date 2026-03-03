<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_reconcile_model_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_reconcile_model_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_account_reconcile_model_search`
- Name: account.reconcile.model.search
- Model: `account.reconcile.model`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_account_reconcile_model_form`
- Name: account.reconcile.model.form
- Model: `account.reconcile.model`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `account_id`, `active`, `amount_string`, `amount_type`, `analytic_distribution`, `company_id`, `label`, `line_ids`, `match_amount`, `match_amount_max`, and 11 more
- Buttons: `action_reconcile_stat`, `action_set_auto_reconcile`, `action_set_manual`
- XPath or positional patches: 0

### `view_account_reconcile_model_tree`
- Name: account.reconcile.model.list
- Model: `account.reconcile.model`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `match_journal_ids`, `name`, `sequence`, `trigger`
- XPath or positional patches: 0

## Actions

- `action_account_reconcile_model`: `act_window` Reconciliation Models

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
