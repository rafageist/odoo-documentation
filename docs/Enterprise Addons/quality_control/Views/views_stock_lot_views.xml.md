---
tags: [odoo, enterprise, generated, views]
---

# views/stock_lot_views.xml

- Module: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]]
- Scope: Enterprise Addons
- Source file: `views/stock_lot_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_production_lot_form_quality_control`
- Name: stock.lot.form.quality
- Model: `stock.lot`
- Type: inferred from arch
- Inherits: `stock.view_production_lot_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `quality_check_qty`
- Buttons: `action_open_quality_checks`
- XPath or positional patches: 1

### `stock_production_lot_view_form`
- Name: stock.production.lot.view.form
- Model: `stock.lot`
- Type: inferred from arch
- Inherits: `stock.view_production_lot_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `quality_alert_qty`
- Buttons: `action_lot_open_quality_alerts`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_control/Views]]

