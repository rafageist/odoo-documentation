<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.post

- Module: [[docs/Enterprise Addons/social/social|social]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/social_post.py`
- Python classes: `SocialPost`
- Description: Social Post
- Inherits: `mail.activity.mixin`, `mail.thread`, `social.post.template`, `utm.source.mixin`

## Field footprint

- Detected fields: 18
- Field types: `Boolean` x 2, `Char` x 1, `Datetime` x 3, `Integer` x 3, `Many2many` x 3, `Many2one` x 3, `One2many` x 1, `Selection` x 2
- Relation fields: 7

## Sample fields

- `account_allowed_ids`: `Many2many` (comodel `social.account`, compute `_compute_account_allowed_ids`)
- `account_ids`: `Many2many`
- `calendar_date`: `Datetime` (comodel `Calendar Date`, compute `_compute_calendar_date`, store `True`)
- `click_count`: `Integer` (comodel `Number of clicks`, compute `_compute_click_count`)
- `company_id`: `Many2one` (comodel `res.company`)
- `engagement`: `Integer` (comodel `Engagement`, compute `_compute_post_engagement`)
- `has_post_errors`: `Boolean` (comodel `There are post errors on sub-posts`, compute `_compute_has_post_errors`)
- `is_hatched`: `Boolean` (compute `_compute_is_hatched`)
- `live_post_ids`: `One2many` (comodel `social.live.post`)
- `live_posts_by_media`: `Char` (comodel `Live Posts by Social Media`, compute `_compute_live_posts_by_media`)
- `media_ids`: `Many2many` (comodel `social.media`, compute `_compute_media_ids`, store `True`)
- `post_method`: `Selection`
- `published_date`: `Datetime` (comodel `Published Date`)
- `scheduled_date`: `Datetime` (comodel `Scheduled Date`)
- `source_id`: `Many2one`
- `state`: `Selection`
- `stream_posts_count`: `Integer` (comodel `Feed Posts Count`, compute `_compute_stream_posts_count`)
- `utm_campaign_id`: `Many2one` (comodel `utm.campaign`)

## Method hints

- Detected methods: 32
- Action methods: `action_post`, `action_redirect_to_clicks`, `action_schedule`, `action_set_draft`
- Compute methods: `_compute_account_allowed_ids`, `_compute_account_ids`, `_compute_calendar_date`, `_compute_click_count`, `_compute_display_name`, `_compute_has_active_accounts`, `_compute_has_post_errors`, `_compute_is_hatched`, and 4 more
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
title social.post - Direct Relations
class "social.post" as social_post
class "res.company" as res_company
class "social.account" as social_account
class "social.live.post" as social_live_post
class "social.media" as social_media
class "utm.campaign" as utm_campaign
social_post .. social_account : account_allowed_ids
social_post --> res_company : company_id
social_post .. social_media : media_ids
social_post --|> social_live_post : live_post_ids
social_post --> utm_campaign : utm_campaign_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/social/Models]]

<!-- GENERATED:MODEL -->
