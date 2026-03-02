<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/account_fleet/account_fleet|account_fleet]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_line_tree_fleet`
- Name: view.move.line.list.fleet
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `vehicle_id`
- XPath or positional patches: 1

### `account_move_view_tree`
- Name: account.move.list.inherit.fleet
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `invoice_date`
- XPath or positional patches: 2

### `view_move_form`
- Name: account.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `need_vehicle`, `vehicle_id`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/account_fleet/Views]]

<!-- GENERATED:VIEWFILE -->
