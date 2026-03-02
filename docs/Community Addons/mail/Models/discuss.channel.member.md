<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# discuss.channel.member

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/discuss/discuss_channel_member.py`
- Python classes: `DiscussChannelMember`
- Description: Channel Member
- Inherits: `bus.listener.mixin`

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 2, `Char` x 1, `Datetime` x 4, `Integer` x 2, `Many2one` x 6, `One2many` x 1, `Selection` x 1
- Relation fields: 7

## Sample fields

- `channel_id`: `Many2one` (comodel `discuss.channel`)
- `custom_channel_name`: `Char` (comodel `Custom channel name`)
- `custom_notifications`: `Selection`
- `fetched_message_id`: `Many2one` (comodel `mail.message`)
- `guest_id`: `Many2one` (comodel `mail.guest`)
- `is_pinned`: `Boolean` (comodel `Is pinned on the interface`, compute `_compute_is_pinned`)
- `is_self`: `Boolean` (compute `_compute_is_self`)
- `last_interest_dt`: `Datetime` (comodel `Last Interest`)
- `last_seen_dt`: `Datetime` (comodel `Last seen date`)
- `message_unread_counter`: `Integer` (comodel `Unread Messages Counter`, compute `_compute_message_unread`)
- `mute_until_dt`: `Datetime` (comodel `Mute notifications until`)
- `new_message_separator`: `Integer`
- `partner_id`: `Many2one` (comodel `res.partner`)
- `rtc_inviting_session_id`: `Many2one` (comodel `discuss.channel.rtc.session`)
- `rtc_session_ids`: `One2many` (comodel `discuss.channel.rtc.session`)
- `seen_message_id`: `Many2one` (comodel `mail.message`)
- `unpin_dt`: `Datetime` (comodel `Unpin date`)

## Method hints

- Detected methods: 32
- Action methods: none
- Compute methods: `_compute_display_name`, `_compute_is_pinned`, `_compute_is_self`, `_compute_message_unread`
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
title discuss.channel.member - Direct Relations
class "discuss.channel.member" as discuss_channel_member
class "discuss.channel" as discuss_channel
class "discuss.channel.rtc.session" as discuss_channel_rtc_session
class "mail.guest" as mail_guest
class "mail.message" as mail_message
class "res.partner" as res_partner
discuss_channel_member --> res_partner : partner_id
discuss_channel_member --> mail_guest : guest_id
discuss_channel_member --> discuss_channel : channel_id
discuss_channel_member --> mail_message : fetched_message_id
discuss_channel_member --> mail_message : seen_message_id
discuss_channel_member --|> discuss_channel_rtc_session : rtc_session_ids
discuss_channel_member --> discuss_channel_rtc_session : rtc_inviting_session_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mail/Models]]

<!-- GENERATED:MODEL -->
