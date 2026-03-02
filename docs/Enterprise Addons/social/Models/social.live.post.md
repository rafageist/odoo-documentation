<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.live.post

- Module: [[docs/Enterprise Addons/social/social|social]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/social_live_post.py`
- Python classes: `SocialLivePost`
- Description: Social Live Post

## Field footprint

- Detected fields: 10
- Field types: `Char` x 2, `Integer` x 1, `Many2many` x 1, `Many2one` x 3, `Selection` x 2, `Text` x 1
- Relation fields: 4

## Sample fields

- `account_id`: `Many2one` (comodel `social.account`)
- `company_id`: `Many2one` (comodel `res.company`, related `account_id.company_id`)
- `engagement`: `Integer` (comodel `Engagement`)
- `failure_reason`: `Text` (comodel `Failure Reason`)
- `image_ids`: `Many2many` (comodel `ir.attachment`, compute `_compute_image_ids`)
- `live_post_link`: `Char` (comodel `Post Link`, compute `_compute_live_post_link`)
- `media_type`: `Selection` (related `account_id.media_type`)
- `message`: `Char` (comodel `Message`, compute `_compute_message`)
- `post_id`: `Many2one` (comodel `social.post`)
- `state`: `Selection`

## Method hints

- Detected methods: 12
- Action methods: `action_retry_post`
- Compute methods: `_compute_display_name`, `_compute_image_ids`, `_compute_live_post_link`, `_compute_message`
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
title social.live.post - Direct Relations
class "social.live.post" as social_live_post
class "ir.attachment" as ir_attachment
class "res.company" as res_company
class "social.account" as social_account
class "social.post" as social_post
social_live_post --> social_post : post_id
social_live_post --> social_account : account_id
social_live_post .. ir_attachment : image_ids
social_live_post --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/social/Models]]

<!-- GENERATED:MODEL -->
