<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# slide.channel.invite

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/slide_channel_invite.py`
- Python classes: `SlideChannelInvite`
- Description: Channel Invitation Wizard
- Inherits: `mail.composer.mixin`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 3, `Char` x 1, `Many2many` x 2, `Many2one` x 1, `Selection` x 1
- Relation fields: 3

## Sample fields

- `attachment_ids`: `Many2many` (comodel `ir.attachment`)
- `channel_id`: `Many2one` (comodel `slide.channel`)
- `channel_invite_url`: `Char` (comodel `Course Link`, compute `_compute_channel_invite_url`)
- `channel_published`: `Boolean` (related `channel_id.is_published`)
- `channel_visibility`: `Selection` (related `channel_id.visibility`)
- `enroll_mode`: `Boolean` (comodel `Enroll partners`)
- `partner_ids`: `Many2many` (comodel `res.partner`)
- `send_email`: `Boolean` (comodel `Send Email`, compute `_compute_send_email`, store `True`)

## Method hints

- Detected methods: 5
- Action methods: `action_invite`
- Compute methods: `_compute_channel_invite_url`, `_compute_render_model`, `_compute_send_email`
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
title slide.channel.invite - Direct Relations
class "slide.channel.invite" as slide_channel_invite
class "ir.attachment" as ir_attachment
class "res.partner" as res_partner
class "slide.channel" as slide_channel
slide_channel_invite .. ir_attachment : attachment_ids
slide_channel_invite .. res_partner : partner_ids
slide_channel_invite --> slide_channel : channel_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Models]]

<!-- GENERATED:MODEL -->
