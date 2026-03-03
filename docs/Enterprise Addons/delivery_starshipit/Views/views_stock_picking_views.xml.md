---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/delivery_starshipit/delivery_starshipit|delivery_starshipit]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_picking_form_inherit_stock`
- Name: stock.picking.form.inherit
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `header`
- Field references: 1
- Sample fields: `carrier_price`
- XPath or positional patches: 1

## Actions

- `action_print_starshipit_labels`: `server` Print Starshipit Labels

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_starshipit/Views]]

