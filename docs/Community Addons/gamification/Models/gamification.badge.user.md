<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# gamification.badge.user

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/gamification_badge_user.py`
- Python classes: `GamificationBadgeUser`
- Description: Gamification User Badge
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 8
- Field types: `Char` x 1, `Many2one` x 5, `Selection` x 1, `Text` x 1
- Relation fields: 5

## Sample fields

- `badge_id`: `Many2one` (comodel `gamification.badge`)
- `badge_name`: `Char` (related `badge_id.name`)
- `challenge_id`: `Many2one` (comodel `gamification.challenge`)
- `comment`: `Text` (comodel `Comment`)
- `level`: `Selection` (related `badge_id.level`, store `True`)
- `sender_id`: `Many2one` (comodel `res.users`)
- `user_id`: `Many2one` (comodel `res.users`)
- `user_partner_id`: `Many2one` (comodel `res.partner`, related `user_id.partner_id`)

## Method hints

- Detected methods: 4
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
title gamification.badge.user - Direct Relations
class "gamification.badge.user" as gamification_badge_user
class "gamification.badge" as gamification_badge
class "gamification.challenge" as gamification_challenge
class "res.partner" as res_partner
class "res.users" as res_users
gamification_badge_user --> res_users : user_id
gamification_badge_user --> res_partner : user_partner_id
gamification_badge_user --> res_users : sender_id
gamification_badge_user --> gamification_badge : badge_id
gamification_badge_user --> gamification_challenge : challenge_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Models]]

<!-- GENERATED:MODEL -->
