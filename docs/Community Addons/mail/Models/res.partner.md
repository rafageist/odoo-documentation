<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.partner

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/discuss/res_partner.py`, `models/res_partner.py`
- Python classes: `ResPartner`
- Inherits: `mail.activity.mixin`, `mail.thread.blacklist`

## Field footprint

- Detected fields: 13
- Field types: `Boolean` x 1, `Char` x 6, `Datetime` x 1, `Many2many` x 1, `Many2one` x 2, `One2many` x 2
- Relation fields: 5

## Sample fields

- `channel_ids`: `Many2many` (comodel `discuss.channel`)
- `channel_member_ids`: `One2many` (comodel `discuss.channel.member`)
- `contact_address_inline`: `Char` (compute `_compute_contact_address_inline`)
- `email`: `Char`
- `im_status`: `Char` (comodel `IM Status`, compute `_compute_im_status`)
- `is_in_call`: `Boolean` (compute `_compute_is_in_call`)
- `name`: `Char`
- `offline_since`: `Datetime` (comodel `Offline since`, compute `_compute_im_status`)
- `parent_id`: `Many2one`
- `phone`: `Char`
- `rtc_session_ids`: `One2many` (comodel `discuss.channel.rtc.session`)
- `user_id`: `Many2one`
- `vat`: `Char`

## Method hints

- Detected methods: 22
- Action methods: none
- Compute methods: `_compute_contact_address_inline`, `_compute_im_status`, `_compute_is_in_call`
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
title res.partner - Direct Relations
class "res.partner" as res_partner
class "discuss.channel" as discuss_channel
class "discuss.channel.member" as discuss_channel_member
class "discuss.channel.rtc.session" as discuss_channel_rtc_session
res_partner .. discuss_channel : channel_ids
res_partner --|> discuss_channel_member : channel_member_ids
res_partner --|> discuss_channel_rtc_session : rtc_session_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mail/Models]]

<!-- GENERATED:MODEL -->
