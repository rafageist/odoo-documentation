<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# discuss.channel.rtc.session

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/discuss/discuss_channel_rtc_session.py`
- Python classes: `DiscussChannelRtcSession`
- Description: Mail RTC session
- Inherits: `bus.listener.mixin`

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 4, `Datetime` x 1, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `channel_id`: `Many2one` (comodel `discuss.channel`, related `channel_member_id.channel_id`, store `True`)
- `channel_member_id`: `Many2one` (comodel `discuss.channel.member`)
- `guest_id`: `Many2one` (comodel `mail.guest`, related `channel_member_id.guest_id`)
- `is_camera_on`: `Boolean`
- `is_deaf`: `Boolean`
- `is_muted`: `Boolean`
- `is_screen_sharing_on`: `Boolean`
- `partner_id`: `Many2one` (comodel `res.partner`, related `channel_member_id.partner_id`, store `True`)
- `write_date`: `Datetime` (comodel `Last Updated On`)

## Method hints

- Detected methods: 11
- Action methods: `action_disconnect`
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
title discuss.channel.rtc.session - Direct Relations
class "discuss.channel.rtc.session" as discuss_channel_rtc_session
class "discuss.channel" as discuss_channel
class "discuss.channel.member" as discuss_channel_member
class "mail.guest" as mail_guest
class "res.partner" as res_partner
discuss_channel_rtc_session --> discuss_channel_member : channel_member_id
discuss_channel_rtc_session --> discuss_channel : channel_id
discuss_channel_rtc_session --> res_partner : partner_id
discuss_channel_rtc_session --> mail_guest : guest_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mail/Models]]

<!-- GENERATED:MODEL -->
