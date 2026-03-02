<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.stream

- Module: [[docs/Enterprise Addons/social/social|social]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/social_stream.py`
- Python classes: `SocialStream`
- Description: Social Stream

## Field footprint

- Detected fields: 9
- Field types: `Binary` x 1, `Char` x 2, `Integer` x 1, `Many2one` x 4, `One2many` x 1
- Relation fields: 5

## Sample fields

- `account_id`: `Many2one` (comodel `social.account`)
- `company_id`: `Many2one` (comodel `res.company`, related `account_id.company_id`, store `True`)
- `media_id`: `Many2one` (comodel `social.media`)
- `media_image`: `Binary` (related `media_id.image`)
- `name`: `Char` (comodel `Title`)
- `sequence`: `Integer` (comodel `Sequence`)
- `stream_post_ids`: `One2many` (comodel `social.stream.post`)
- `stream_type_id`: `Many2one` (comodel `social.stream.type`)
- `stream_type_type`: `Char` (related `stream_type_id.stream_type`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: none
- Onchange methods: `_onchange_media_id`

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
title social.stream - Direct Relations
class "social.stream" as social_stream
class "res.company" as res_company
class "social.account" as social_account
class "social.media" as social_media
class "social.stream.post" as social_stream_post
class "social.stream.type" as social_stream_type
social_stream --> social_media : media_id
social_stream --> social_account : account_id
social_stream --> social_stream_type : stream_type_id
social_stream --|> social_stream_post : stream_post_ids
social_stream --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/social/Models]]

<!-- GENERATED:MODEL -->
