---
tags: [odoo, community, generated, views]
---

# views/mailing_mailing_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/mailing_mailing_views.xml`
- Views: 5
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `mailing_mailing_view_calendar`
- Name: mailing.mailing.view.calendar
- Model: `mailing.mailing`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `mailing_model_id`, `state`, `user_id`
- XPath or positional patches: 0

### `view_mail_mass_mailing_kanban`
- Name: mailing.mailing.kanban
- Model: `mailing.mailing`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `active`, `campaign_id`, `color`, `mailing_model_id`, `mailing_on_mailing_list`, `next_departure`, `schedule_date`, `sent_date`, `subject`, `total`, and 1 more
- XPath or positional patches: 0

### `view_mail_mass_mailing_form`
- Name: mailing.mailing.form
- Model: `mailing.mailing`
- Type: inferred from arch
- Root tag: `form`
- Field references: 52
- Sample fields: `ab_testing_completed`, `ab_testing_description`, `ab_testing_enabled`, `ab_testing_mailings_count`, `ab_testing_pc`, `ab_testing_schedule_datetime`, `ab_testing_winner_selection`, `active`, `attachment_ids`, `body_arch`, and 42 more
- Buttons: `action_cancel`, `action_compare_versions`, `action_duplicate`, `action_launch`, `action_reload`, `action_remove_favorite`, `action_retry_failed`, `action_schedule`, `action_select_as_winner`, `action_send_winner_mailing`, and 14 more
- XPath or positional patches: 0

### `view_mail_mass_mailing_tree`
- Name: mailing.mailing.list
- Model: `mailing.mailing`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `ab_testing_enabled`, `bounced_ratio`, `calendar_date`, `campaign_id`, `clicks_ratio`, `mailing_model_id`, `opened_ratio`, `received_ratio`, `replied_ratio`, `sent`, and 3 more
- XPath or positional patches: 0

### `view_mail_mass_mailing_search`
- Name: mailing.mailing.search
- Model: `mailing.mailing`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `campaign_id`, `name`
- XPath or positional patches: 0

## Actions

- `action_ab_testing_open_winner_mailing`: `act_window` A/B Test Winner
- `action_create_mass_mailings_from_campaign`: `act_window` Mailings
- `action_view_mass_mailings_from_campaign`: `act_window` Mailings
- `mailing_mailing_action_mail_fullwidth_calendar`: `view`
- `mailing_mailing_action_mail_fullwidth_kanban`: `view`
- `mailing_mailing_action_mail_fullwidth_tree`: `view`
- `mailing_mailing_action_mail`: `act_window` Mailings

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

