<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.group

- Module: [[docs/Community Addons/mail_group/mail_group|mail_group]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mail_group.py`
- Python classes: `MailGroup`
- Description: Mail Group
- Inherits: `mail.alias.mixin`

## Field footprint

- Detected fields: 25
- Field types: `Boolean` x 8, `Char` x 1, `Html` x 2, `Image` x 1, `Integer` x 5, `Many2many` x 2, `Many2one` x 1, `One2many` x 3, `Selection` x 1, `Text` x 1
- Relation fields: 6

## Sample fields

- `access_group_id`: `Many2one` (comodel `res.groups`)
- `access_mode`: `Selection`
- `active`: `Boolean` (comodel `Active`)
- `can_manage_group`: `Boolean` (comodel `Can Manage`, compute `_compute_can_manage_group`)
- `description`: `Text` (comodel `Description`)
- `image_128`: `Image` (comodel `Image`)
- `is_closed`: `Boolean` (comodel `Is Closed`)
- `is_member`: `Boolean` (comodel `Is Member`, compute `_compute_is_member`)
- `is_moderator`: `Boolean` (compute `_compute_is_moderator`)
- `mail_group_message_count`: `Integer` (comodel `Messages Count`, compute `_compute_mail_group_message_count`)
- `mail_group_message_ids`: `One2many` (comodel `mail.group.message`)
- `mail_group_message_last_month_count`: `Integer` (comodel `Messages Per Month`, compute `_compute_mail_group_message_last_month_count`)
- `mail_group_message_moderation_count`: `Integer` (comodel `Pending Messages Count`, compute `_compute_mail_group_message_moderation_count`)
- `member_count`: `Integer` (comodel `Members Count`, compute `_compute_member_count`)
- `member_ids`: `One2many` (comodel `mail.group.member`)
- `member_partner_ids`: `Many2many` (comodel `res.partner`, compute `_compute_member_partner_ids`)
- `moderation`: `Boolean`
- `moderation_guidelines`: `Boolean`
- `moderation_guidelines_msg`: `Html`
- `moderation_notify`: `Boolean`

## Method hints

- Detected methods: 44
- Action methods: `action_close`, `action_join`, `action_leave`, `action_open`, `action_send_guidelines`
- Compute methods: `_compute_can_manage_group`, `_compute_is_member`, `_compute_is_moderator`, `_compute_mail_group_message_count`, `_compute_mail_group_message_last_month_count`, `_compute_mail_group_message_moderation_count`, `_compute_member_count`, `_compute_member_partner_ids`, and 1 more
- Onchange methods: `_onchange_access_mode`, `_onchange_moderation`

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
title mail.group - Direct Relations
class "mail.group" as mail_group
class "mail.group.member" as mail_group_member
class "mail.group.message" as mail_group_message
class "mail.group.moderation" as mail_group_moderation
class "res.groups" as res_groups
class "res.partner" as res_partner
class "res.users" as res_users
mail_group --|> mail_group_message : mail_group_message_ids
mail_group --|> mail_group_member : member_ids
mail_group .. res_partner : member_partner_ids
mail_group --|> mail_group_moderation : moderation_rule_ids
mail_group .. res_users : moderator_ids
mail_group --> res_groups : access_group_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mail_group/Models]]

<!-- GENERATED:MODEL -->
