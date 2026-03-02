<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.users

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_users.py`
- Python classes: `ResUsers`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 2, `Char` x 1, `Integer` x 1, `Many2many` x 3
- Relation fields: 3

## Sample fields

- `has_access_livechat`: `Boolean` (compute `_compute_has_access_livechat`, store `False`)
- `livechat_channel_ids`: `Many2many` (comodel `im_livechat.channel`)
- `livechat_expertise_ids`: `Many2many` (comodel `im_livechat.expertise`, compute `_compute_livechat_expertise_ids`, store `False`)
- `livechat_is_in_call`: `Boolean` (compute `_compute_livechat_is_in_call`)
- `livechat_lang_ids`: `Many2many` (comodel `res.lang`, compute `_compute_livechat_lang_ids`, store `False`)
- `livechat_ongoing_session_count`: `Integer` (comodel `Number of Ongoing sessions`, compute `_compute_livechat_ongoing_session_count`)
- `livechat_username`: `Char` (compute `_compute_livechat_username`, store `False`)

## Method hints

- Detected methods: 13
- Action methods: none
- Compute methods: `_compute_has_access_livechat`, `_compute_livechat_expertise_ids`, `_compute_livechat_is_in_call`, `_compute_livechat_lang_ids`, `_compute_livechat_ongoing_session_count`, `_compute_livechat_username`
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
title res.users - Direct Relations
class "res.users" as res_users
class "im_livechat.channel" as im_livechat_channel
class "im_livechat.expertise" as im_livechat_expertise
class "res.lang" as res_lang
res_users .. im_livechat_channel : livechat_channel_ids
res_users .. res_lang : livechat_lang_ids
res_users .. im_livechat_expertise : livechat_expertise_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Models]]

<!-- GENERATED:MODEL -->
