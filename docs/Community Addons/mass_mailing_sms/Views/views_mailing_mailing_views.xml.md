---
tags: [odoo, community, generated, views]
---

# views/mailing_mailing_views.xml

- Module: [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]]
- Scope: Community Addons
- Source file: `views/mailing_mailing_views.xml`
- Views: 5
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `mailing_mailing_view_tree_sms`
- Name: mailing.mailing.view.list.sms
- Model: `mailing.mailing`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `ab_testing_enabled`, `bounced`, `calendar_date`, `campaign_id`, `clicked`, `mailing_model_id`, `mailing_type`, `sent`, `state`, `subject`, and 1 more
- XPath or positional patches: 0

### `mailing_mailing_view_kanban_sms`
- Name: mailing.mailing.view.kanban.inherit.sms
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `mass_mailing.view_mail_mass_mailing_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sms_has_insufficient_credit`, `sms_has_unregistered_account`
- XPath or positional patches: 2

### `mailing_mailing_view_form_mixed`
- Name: mailing.mailing.view.form.mixed
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `mass_mailing_sms.mailing_mailing_view_form_sms`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mailing_mailing_view_form_sms`
- Name: mailing.mailing.view.form.inherit.sms
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `mass_mailing.view_mail_mass_mailing_form`
- Root tag: `xpath`
- Field references: 10
- Sample fields: `ab_testing_mailings_sms_count`, `ab_testing_schedule_datetime`, `ab_testing_sms_winner_selection`, `body_plaintext`, `schedule_type`, `sms_allow_unsubscribe`, `sms_force_send`, `sms_has_insufficient_credit`, `sms_has_unregistered_account`, `sms_subject`
- Buttons: `action_buy_sms_credits`, `action_put_in_queue`, `action_send_mail`
- XPath or positional patches: 40

### `mailing_mailing_view_search_sms`
- Name: mailing.mailing.search
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `mass_mailing.view_mail_mass_mailing_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `mailing_mailing_action_sms_view_kanban`: `view`
- `mailing_mailing_action_sms_view_tree`: `view`
- `mailing_mailing_action_sms`: `act_window` SMS Marketing

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sms/Views]]

