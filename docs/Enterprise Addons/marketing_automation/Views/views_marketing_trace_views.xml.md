---
tags: [odoo, enterprise, generated, views]
---

# views/marketing_trace_views.xml

- Module: [[docs/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]]
- Scope: Enterprise Addons
- Source file: `views/marketing_trace_views.xml`
- Views: 5
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `marketing_trace_view_search`
- Name: marketing.trace.view.search
- Model: `marketing.trace`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `activity_id`, `participant_id`
- XPath or positional patches: 0

### `marketing_trace_view_pivot`
- Name: marketing.trace.view.pivot
- Model: `marketing.trace`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `activity_id`, `state`
- XPath or positional patches: 0

### `marketing_trace_view_graph`
- Name: marketing.trace.view.graph
- Model: `marketing.trace`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `activity_id`, `state`
- XPath or positional patches: 0

### `marketing_trace_view_tree`
- Name: marketing.trace.view.list
- Model: `marketing.trace`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `activity_id`, `is_test`, `participant_id`, `schedule_date`, `state`
- XPath or positional patches: 0

### `marketing_trace_view_form`
- Name: marketing.trace.view.form
- Model: `marketing.trace`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `activity_id`, `mailing_trace_ids`, `participant_id`, `schedule_date`, `state`, `state_msg`
- XPath or positional patches: 0

## Actions

- `marketing_trace_action`: `act_window` Traces

## Menus

- `marketing_trace_menu`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/marketing_automation/Views]]

