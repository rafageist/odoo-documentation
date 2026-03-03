---
tags: [odoo, community, generated, views]
---

# report/mailing_trace_report_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `report/mailing_trace_report_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mailing_trace_report_view_search`
- Name: mailing.trace.report.view.search
- Model: `mailing.trace.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `campaign`, `name`, `scheduled_date`
- XPath or positional patches: 0

### `mailing_trace_report_view_graph`
- Name: mailing.trace.report.view.graph
- Model: `mailing.trace.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `clicked`, `name`, `replied`, `sent`
- XPath or positional patches: 0

### `mailing_trace_report_view_pivot`
- Name: mailing.trace.report.view.pivot
- Model: `mailing.trace.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 10
- Sample fields: `bounced`, `canceled`, `clicked`, `delivered`, `error`, `name`, `opened`, `replied`, `scheduled`, `sent`
- XPath or positional patches: 0

### `mailing_trace_report_view_tree`
- Name: mailing.trace.report.view.list
- Model: `mailing.trace.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 16
- Sample fields: `bounced`, `campaign`, `canceled`, `clicked`, `delivered`, `error`, `mailing_type`, `name`, `opened`, `pending`, and 6 more
- XPath or positional patches: 0

## Actions

- `mailing_trace_report_action_mail`: `act_window` Mass Mailing Analysis

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

