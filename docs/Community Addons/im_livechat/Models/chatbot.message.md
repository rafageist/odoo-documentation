<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# chatbot.message

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/chatbot_message.py`
- Python classes: `ChatbotMessage`
- Description: Chatbot Message

## Field footprint

- Detected fields: 6
- Field types: `Html` x 1, `Integer` x 1, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `discuss_channel_id`: `Many2one` (comodel `discuss.channel`)
- `mail_message_id`: `Many2one` (comodel `mail.message`)
- `script_step_id`: `Many2one` (comodel `chatbot.script.step`)
- `user_raw_answer`: `Html`
- `user_raw_script_answer_id`: `Integer`
- `user_script_answer_id`: `Many2one` (comodel `chatbot.script.answer`)

## Method hints

- Detected methods: 0
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
title chatbot.message - Direct Relations
class "chatbot.message" as chatbot_message
class "chatbot.script.answer" as chatbot_script_answer
class "chatbot.script.step" as chatbot_script_step
class "discuss.channel" as discuss_channel
class "mail.message" as mail_message
chatbot_message --> mail_message : mail_message_id
chatbot_message --> discuss_channel : discuss_channel_id
chatbot_message --> chatbot_script_step : script_step_id
chatbot_message --> chatbot_script_answer : user_script_answer_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Models]]

<!-- GENERATED:MODEL -->
