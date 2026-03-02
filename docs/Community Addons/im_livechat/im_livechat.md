<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Live Chat

- Scope: Community Addons
- Source: odoo/addons/im_livechat
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/rating/rating|rating]], [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/utm/utm|utm]]

## Summary

Chat with your website visitors

## Generated coverage

- Models: 22
- XML files with UI/data artifacts: 14
- Views: 40
- Actions: 25
- Menus: 15
- Rules (ir.rule): 3
- Access CSV entries: 15
- Controller units: 15
- Frontend asset files: 129

## Module map

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
title Live Chat - Generated Coverage
component "Module Overview" as overview
component "Models\n22" as models
component "Views / XML\n40 views\n14 files" as views
component "Controllers\n50 routes" as controllers
component "Frontend\n129 files" as frontend
component "Security / Data\n3 rules\n15 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/im_livechat/Models|Models]] (22)
- Views and XML: [[docs/Community Addons/im_livechat/Views|Views]] (14 files)
- Controllers: [[docs/Community Addons/im_livechat/Controllers|Controllers]] (15)
- Frontend: [[docs/Community Addons/im_livechat/Frontend|Frontend]] (129 files)

## Key models

- `chatbot.message`
- `chatbot.script`
- `chatbot.script.answer`
- `chatbot.script.step`
- `digest.digest`
- `discuss.call.history`
- `discuss.channel`
- `discuss.channel.member`
- `discuss.channel.rtc.session`
- `im_livechat.channel`
- `im_livechat.channel.member.history`
- `im_livechat.channel.rule`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






