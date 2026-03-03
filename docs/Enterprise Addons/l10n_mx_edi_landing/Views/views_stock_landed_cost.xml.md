---
tags: [odoo, enterprise, generated, views]
---

# views/stock_landed_cost.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi_landing/l10n_mx_edi_landing|l10n_mx_edi_landing]]
- Scope: Enterprise Addons
- Source file: `views/stock_landed_cost.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_landed_cost_l10n_mx_stock_search`
- Name: stock_landed_cost_l10n_mx_stock.search
- Model: `stock.landed.cost`
- Type: inferred from arch
- Inherits: `stock_landed_costs.view_stock_landed_cost_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_mx_edi_customs_number`
- XPath or positional patches: 1

### `view_stock_landed_cost_form_l10n_mx_stock`
- Name: view.stock.landed.cost.form.l10n_mx_stock
- Model: `stock.landed.cost`
- Type: inferred from arch
- Inherits: `stock_landed_costs.view_stock_landed_cost_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `fiscal_country_codes`, `l10n_mx_edi_customs_number`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi_landing/Views]]

