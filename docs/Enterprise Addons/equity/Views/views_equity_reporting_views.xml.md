---
tags: [odoo, enterprise, generated, views]
---

# views/equity_reporting_views.xml

- Module: [[docs/Enterprise Addons/equity/equity|equity]]
- Scope: Enterprise Addons
- Source file: `views/equity_reporting_views.xml`
- Views: 1
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `view_equity_cap_table_pivot`
- Name: equity.cap.table.pivot
- Model: `equity.cap.table`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `holder_id`, `securities`, `security_class_id`
- XPath or positional patches: 0

## Actions

- `action_equity_valuation_graph`: `client` Valuation
- `action_equity_cap_table`: `client` Cap Table
- `action_equity_cap_table_pivot`: `act_window` Cap Table Pivot

## Navigation

- **Parent:** [[docs/Enterprise Addons/equity/Views]]

