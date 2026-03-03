---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_spreadsheet_views.xml

- Module: [[docs/Enterprise Addons/spreadsheet_sale_management/spreadsheet_sale_management|spreadsheet_sale_management]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_spreadsheet_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `sale_order_spreadsheet_view_search`
- Name: sale.order.spreadsheet search view
- Model: `sale.order.spreadsheet`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

### `sale_order_spreadsheet_view_list`
- Name: sale.order.spreadsheet list view
- Model: `sale.order.spreadsheet`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `name`, `order_id`, `spreadsheet_binary_data`, `spreadsheet_file_name`
- XPath or positional patches: 0

## Actions

- `sale_order_spreadsheet_action`: `act_window` Sale Order Spreadsheets

## Menus

- `menu_technical_spreadsheet_sale_order_template`: Sale Order Spreadsheets

## Navigation

- **Parent:** [[docs/Enterprise Addons/spreadsheet_sale_management/Views]]

