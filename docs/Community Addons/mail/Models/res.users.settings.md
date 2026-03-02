<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.users.settings

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_users_settings.py`
- Python classes: `ResUsersSettings`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 3, `Char` x 1, `Integer` x 1, `One2many` x 1, `Selection` x 1
- Relation fields: 1

## Sample fields

- `channel_notifications`: `Selection`
- `is_discuss_sidebar_category_channel_open`: `Boolean`
- `is_discuss_sidebar_category_chat_open`: `Boolean`
- `push_to_talk_key`: `Char`
- `use_push_to_talk`: `Boolean`
- `voice_active_duration`: `Integer`
- `volume_settings_ids`: `One2many` (comodel `res.users.settings.volumes`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: none
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
title res.users.settings - Direct Relations
class "res.users.settings" as res_users_settings
class "res.users.settings.volumes" as res_users_settings_volumes
res_users_settings --|> res_users_settings_volumes : volume_settings_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mail/Models]]

<!-- GENERATED:MODEL -->
