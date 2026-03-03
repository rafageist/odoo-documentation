---
tags: [odoo, enterprise, generated, views]
---

# views/frontdesk_report_views.xml

- Module: [[docs/Enterprise Addons/frontdesk/frontdesk|frontdesk]]
- Scope: Enterprise Addons
- Source file: `views/frontdesk_report_views.xml`
- Views: 3
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `frontdesk_station_report_view_graph`
- Name: frontdesk.station.report.graph
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `check_in`, `duration`
- XPath or positional patches: 0

### `frontdesk_drink_report_view_graph`
- Name: frontdesk.drink.report.graph
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `drink_ids`, `duration`
- XPath or positional patches: 0

### `frontdesk_visitor_report_view_graph`
- Name: frontdesk.visitor.report.graph
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `check_in`, `duration`
- XPath or positional patches: 0

## Actions

- `action_frontdesk_drinks_report`: `act_window` Drinks
- `action_frontdesk_visitors_report`: `act_window` Visitors
- `action_frontdesk_station_report`: `act_window` Statistics

## Navigation

- **Parent:** [[docs/Enterprise Addons/frontdesk/Views]]

