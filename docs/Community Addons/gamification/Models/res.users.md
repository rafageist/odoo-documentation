<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.users

- Module: [[docs/Community Addons/gamification/gamification|gamification]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_users.py`
- Python classes: `ResUsers`

## Field footprint

- Detected fields: 8
- Field types: `Integer` x 4, `Many2one` x 2, `One2many` x 2
- Relation fields: 4

## Sample fields

- `badge_ids`: `One2many` (comodel `gamification.badge.user`)
- `bronze_badge`: `Integer` (comodel `Bronze badges count`, compute `_get_user_badge_level`)
- `gold_badge`: `Integer` (comodel `Gold badges count`, compute `_get_user_badge_level`)
- `karma`: `Integer` (comodel `Karma`, compute `_compute_karma`, store `True`)
- `karma_tracking_ids`: `One2many` (comodel `gamification.karma.tracking`)
- `next_rank_id`: `Many2one` (comodel `gamification.karma.rank`)
- `rank_id`: `Many2one` (comodel `gamification.karma.rank`)
- `silver_badge`: `Integer` (comodel `Silver badges count`, compute `_get_user_badge_level`)

## Method hints

- Detected methods: 14
- Action methods: `action_karma_report`
- Compute methods: `_compute_karma`
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
class "gamification.badge.user" as gamification_badge_user
class "gamification.karma.rank" as gamification_karma_rank
class "gamification.karma.tracking" as gamification_karma_tracking
res_users --|> gamification_karma_tracking : karma_tracking_ids
res_users --|> gamification_badge_user : badge_ids
res_users --> gamification_karma_rank : rank_id
res_users --> gamification_karma_rank : next_rank_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/gamification/Models]]

<!-- GENERATED:MODEL -->
