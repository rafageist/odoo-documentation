<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mailing.mailing

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mailing.py`
- Python classes: `MailingMailing`
- Description: Mass Mailing
- Inherits: `mail.activity.mixin`, `mail.render.mixin`, `mail.thread`, `utm.source.mixin`

## Field footprint

- Detected fields: 69
- Field types: `Boolean` x 13, `Char` x 10, `Datetime` x 6, `Float` x 5, `Html` x 3, `Integer` x 18, `Many2many` x 2, `Many2one` x 6, `One2many` x 1, `Selection` x 5
- Relation fields: 9

## Sample fields

- `ab_testing_completed`: `Boolean` (related `campaign_id.ab_testing_completed`)
- `ab_testing_description`: `Html` (comodel `A/B Testing Description`, compute `_compute_ab_testing_description`)
- `ab_testing_enabled`: `Boolean`
- `ab_testing_is_winner_mailing`: `Boolean` (comodel `Is the Winner of its Campaign`, compute `_compute_ab_testing_is_winner_mailing`)
- `ab_testing_mailings_count`: `Integer` (related `campaign_id.ab_testing_mailings_count`)
- `ab_testing_pc`: `Integer`
- `ab_testing_schedule_datetime`: `Datetime` (related `campaign_id.ab_testing_schedule_datetime`)
- `ab_testing_winner_selection`: `Selection` (related `campaign_id.ab_testing_winner_selection`)
- `active`: `Boolean`
- `attachment_ids`: `Many2many` (comodel `ir.attachment`)
- `body_arch`: `Html`
- `body_html`: `Html`
- `bounced`: `Integer` (compute `_compute_statistics`)
- `bounced_ratio`: `Float` (compute `_compute_statistics`)
- `calendar_date`: `Datetime` (comodel `Calendar Date`, compute `_compute_calendar_date`, store `True`)
- `campaign_id`: `Many2one` (comodel `utm.campaign`)
- `canceled`: `Integer` (compute `_compute_statistics`)
- `clicked`: `Integer` (compute `_compute_statistics`)
- `clicks_ratio`: `Float` (compute `_compute_clicks_ratio`)
- `color`: `Integer`

## Method hints

- Detected methods: 91
- Action methods: `action_cancel`, `action_compare_versions`, `action_duplicate`, `action_fetch_favorites`, `action_launch`, `action_put_in_queue`, `action_reload`, `action_remove_favorite`, and 19 more
- Compute methods: `_compute_ab_testing_description`, `_compute_ab_testing_is_winner_mailing`, `_compute_calendar_date`, `_compute_clicks_ratio`, `_compute_email_from`, `_compute_favorite_date`, `_compute_is_ab_test_sent`, `_compute_is_body_empty`, and 17 more
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title mailing.mailing - Direct Relations
class "mailing.mailing" as mailing_mailing
class "ir.attachment" as ir_attachment
class "ir.mail_server" as ir_mail_server
class "ir.model" as ir_model
class "mailing.filter" as mailing_filter
class "mailing.list" as mailing_list
class "mailing.trace" as mailing_trace
class "res.users" as res_users
class "utm.campaign" as utm_campaign
class "utm.medium" as utm_medium
mailing_mailing .. ir_attachment : attachment_ids
mailing_mailing --> utm_campaign : campaign_id
mailing_mailing --> utm_medium : medium_id
mailing_mailing --> res_users : user_id
mailing_mailing --> ir_model : mailing_model_id
mailing_mailing --> ir_mail_server : mail_server_id
mailing_mailing .. mailing_list : contact_list_ids
mailing_mailing --> mailing_filter : mailing_filter_id
mailing_mailing --|> mailing_trace : mailing_trace_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Models]]

<!-- GENERATED:MODEL -->
