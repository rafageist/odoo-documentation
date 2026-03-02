<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/documents_account/documents_account|documents_account]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_move_view_form`
- Name: account.move.view.form.inherit.document
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_view_documents_account_move`
- XPath or positional patches: 1

### `view_account_move_form_inherit_documents_account`
- Name: account.move.form.inherit.documents_account
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `suspense_statement_line_id`
- Buttons: `button_reconcile_with_st_line`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_account/Views]]

<!-- GENERATED:VIEWFILE -->
