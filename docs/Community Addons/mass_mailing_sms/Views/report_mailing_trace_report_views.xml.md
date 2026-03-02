<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/mailing_trace_report_views.xml

- Module: [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]]
- Scope: Community Addons
- Source file: `report/mailing_trace_report_views.xml`
- Views: 3
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `mailing_trace_report_sms_view_graph`
- Name: mailing.sms.trace.report.view.graph
- Model: `mailing.trace.report`
- Type: `graph`
- Inherits: `mass_mailing.mailing_trace_report_view_graph`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mailing_trace_report_sms_view_pivot`
- Name: mailing.sms.trace.report.view.pivot
- Model: `mailing.trace.report`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_trace_report_view_pivot`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `mailing_trace_report_sms_view_tree`
- Name: mailing.sms.trace.report.view.list
- Model: `mailing.trace.report`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_trace_report_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

## Actions

- `mailing_trace_report_action_sms_view_tree`: `view`
- `mailing_trace_report_action_sms_view_pivot`: `view`
- `mailing_trace_report_action_sms_view_graph`: `view`
- `mailing_trace_report_action_sms`: `act_window` SMS Marketing Analysis

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sms/Views]]

<!-- GENERATED:VIEWFILE -->
