<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Website Live Chat

- Scope: Community Addons
- Source: odoo/addons/website_livechat
- Dependencies: [[docs/Community Addons/website/website|website]], [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]

## Summary

Chat with your website visitors

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 4
- Views: 7
- Actions: 5
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2
- Controller units: 1
- Frontend asset files: 9

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
title Website Live Chat - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n7 views\n4 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n9 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_livechat/Models|Models]] (8)
- Views and XML: [[docs/Community Addons/website_livechat/Views|Views]] (4 files)
- Controllers: [[docs/Community Addons/website_livechat/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_livechat/Frontend|Frontend]] (9 files)

## Key models

- `chatbot.script`
- `chatbot.script.step`
- `discuss.channel`
- `im_livechat.channel`
- `ir.http`
- `res.config.settings`
- `website`
- `website.visitor`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




