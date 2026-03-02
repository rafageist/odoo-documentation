<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mailing_trace_views.xml

- Module: [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]]
- Scope: Community Addons
- Source file: `views/mailing_trace_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mailing_trace_view_form_sms`
- Name: mailing.trace.view.form.sms
- Model: `mailing.trace`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `campaign_id`, `failure_type`, `is_test_trace`, `links_click_datetime`, `mass_mailing_id`, `medium_id`, `open_datetime`, `reply_datetime`, `sent_datetime`, `sms_code`, and 6 more
- Buttons: `action_view_contact`
- XPath or positional patches: 0

### `mailing_trace_view_form`
- Name: mailing.trace.view.form.inherit.sms
- Model: `mailing.trace`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_trace_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `sms_code`, `sms_id_int`, `sms_number`
- XPath or positional patches: 6

### `mailing_trace_view_tree_sms`
- Name: mailing.trace.view.list.sms
- Model: `mailing.trace`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `failure_type`, `is_test_trace`, `links_click_datetime`, `mass_mailing_id`, `open_datetime`, `reply_datetime`, `sent_datetime`, `sms_number`, `trace_status`
- Buttons: `action_view_contact`
- XPath or positional patches: 0

### `mailing_trace_view_tree`
- Name: mailing.trace.view.list.inherit.sms
- Model: `mailing.trace`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_trace_view_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sms_number`, `trace_type`
- XPath or positional patches: 2

### `mailing_trace_view_search`
- Name: mailing.trace.view.search.inherit.sms
- Model: `mailing.trace`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_trace_view_search`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `sms_id`, `sms_id_int`, `sms_number`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sms/Views]]

<!-- GENERATED:VIEWFILE -->
