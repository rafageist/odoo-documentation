<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# discuss.channel.member

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/discuss_channel_member.py`
- Python classes: `DiscussChannelMember`

## Field footprint

- Detected fields: 4
- Field types: `Many2many` x 1, `Many2one` x 1, `One2many` x 1, `Selection` x 1
- Relation fields: 3

## Sample fields

- `agent_expertise_ids`: `Many2many` (comodel `im_livechat.expertise`, compute `_compute_agent_expertise_ids`)
- `chatbot_script_id`: `Many2one` (comodel `chatbot.script`, compute `_compute_chatbot_script_id`)
- `livechat_member_history_ids`: `One2many` (comodel `im_livechat.channel.member.history`)
- `livechat_member_type`: `Selection` (compute `_compute_livechat_member_type`)

## Method hints

- Detected methods: 15
- Action methods: none
- Compute methods: `_compute_agent_expertise_ids`, `_compute_chatbot_script_id`, `_compute_livechat_member_type`
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
class "chatbot.script" as chatbot_script
class "im_livechat.channel.member.history" as im_livechat_channel_member_history
class "im_livechat.expertise" as im_livechat_expertise
discuss_channel_member --|> im_livechat_channel_member_history : livechat_member_history_ids
discuss_channel_member --> chatbot_script : chatbot_script_id
discuss_channel_member .. im_livechat_expertise : agent_expertise_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Models]]

<!-- GENERATED:MODEL -->
