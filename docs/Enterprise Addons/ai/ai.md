<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# AI

- Scope: Enterprise Addons
- Source: enterprise/ai
- Dependencies: [[docs/Community Addons/mail/mail|mail]]

## Summary

Base module for AI features

## Generated coverage

- Models: 17
- XML files with UI/data artifacts: 6
- Views: 5
- Actions: 10
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 12
- Controller units: 2
- Frontend asset files: 71

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
title AI - Generated Coverage
component "Module Overview" as overview
component "Models\n17" as models
component "Views / XML\n5 views\n6 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n71 files" as frontend
component "Security / Data\n0 rules\n12 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/ai/Models|Models]] (17)
- Views and XML: [[docs/Enterprise Addons/ai/Views|Views]] (6 files)
- Controllers: [[docs/Enterprise Addons/ai/Controllers|Controllers]] (2)
- Frontend: [[docs/Enterprise Addons/ai/Frontend|Frontend]] (71 files)

## Key models

- `ai.agent`
- `ai.agent.source`
- `ai.composer`
- `ai.embedding`
- `ai.prompt.button`
- `ai.topic`
- `base`
- `discuss.channel`
- `ir.actions.server`
- `ir.attachment`
- `ir.http`
- `mail.composer.mixin`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





