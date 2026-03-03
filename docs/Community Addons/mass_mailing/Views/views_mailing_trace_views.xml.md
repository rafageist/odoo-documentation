---
tags: [odoo, community, generated, views]
---

# views/mailing_trace_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/mailing_trace_views.xml`
- Views: 5
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_mail_mail_statistics_graph`
- Name: Mail Statistics Graph
- Model: `mailing.trace`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `trace_status`, `write_date`
- XPath or positional patches: 0

### `mailing_trace_view_form`
- Name: mailing.trace.view.form
- Model: `mailing.trace`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `campaign_id`, `email`, `failure_reason`, `failure_type`, `is_test_trace`, `links_click_datetime`, `mail_mail_id_int`, `mass_mailing_id`, `medium_id`, `message_id`, and 6 more
- Buttons: `action_view_contact`
- XPath or positional patches: 0

### `mailing_trace_view_tree_mail`
- Name: mailing.trace.view.list.mail
- Model: `mailing.trace`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `email`, `failure_type`, `is_test_trace`, `links_click_datetime`, `mass_mailing_id`, `message_id`, `open_datetime`, `reply_datetime`, `sent_datetime`, `trace_status`
- Buttons: `action_view_contact`
- XPath or positional patches: 0

### `mailing_trace_view_tree`
- Name: mailing.trace.view.list
- Model: `mailing.trace`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `email`, `failure_type`, `is_test_trace`, `links_click_datetime`, `mass_mailing_id`, `message_id`, `open_datetime`, `reply_datetime`, `sent_datetime`, `trace_status`
- Buttons: `action_view_contact`
- XPath or positional patches: 0

### `mailing_trace_view_search`
- Name: mailing.trace.view.search
- Model: `mailing.trace`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `email`, `mail_mail_id_int`, `mass_mailing_id`, `message_id`
- XPath or positional patches: 0

## Actions

- `action_view_mail_mail_statistics_mailing`: `act_window` Mail Statistics
- `mailing_trace_action`: `act_window` Mailing Traces

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

