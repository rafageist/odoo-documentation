---
tags: [odoo, community, generated, views]
---

# views/pos_printer_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_printer_view.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_pos_printer`
- Name: Preparation Printers
- Model: `pos.printer`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `name`, `product_categories_ids`, `proxy_ip`
- XPath or positional patches: 0

### `view_pos_printer_form`
- Name: Preparation Printer
- Model: `pos.printer`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `epson_printer_ip`, `name`, `printer_type`, `product_categories_ids`, `proxy_ip`
- XPath or positional patches: 0

## Actions

- `action_pos_printer_form`: `act_window` Preparation Printers

## Menus

- `point_of_sale.menu_pos_preparation_printer`: Preparation Printers

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

