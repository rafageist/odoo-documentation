<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# CRM Livechat

- Scope: Community Addons
- Source: odoo/addons/crm_livechat
- Dependencies: [[docs/Community Addons/crm/crm|crm]], [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]

## Summary

Create lead from livechat conversation

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 5
- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 4

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
title CRM Livechat - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n4 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n2 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/crm_livechat/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/crm_livechat/Views|Views]] (5 files)
- Frontend: [[docs/Community Addons/crm_livechat/Frontend|Frontend]] (4 files)

## Key models

- `chatbot.script`
- `chatbot.script.step`
- `crm.lead`
- `discuss.channel`
- `im_livechat.report.channel`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






