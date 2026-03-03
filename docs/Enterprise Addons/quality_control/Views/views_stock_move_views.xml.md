---
tags: [odoo, enterprise, generated, views]
---

# views/stock_move_views.xml

- Module: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]]
- Scope: Enterprise Addons
- Source file: `views/stock_move_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_move_line_detailed_operation_tree_inherit_quality`
- Name: stock.move.line.operations.list.inherit
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_line_detailed_operation_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `check_state`
- Buttons: `action_open_quality_check_wizard`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_control/Views]]

