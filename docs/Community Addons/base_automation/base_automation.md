<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Automation Rules

- Scope: Community Addons
- Source: odoo/addons/base_automation
- Dependencies: base (not documented), [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/resource/resource|resource]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/sms/sms|sms]]

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 2
- Views: 5
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 1
- Frontend asset files: 8

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
title Automation Rules - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n5 views\n2 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n8 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/base_automation/Models|Models]] (3)
- Views and XML: [[docs/Community Addons/base_automation/Views|Views]] (2 files)
- Controllers: [[docs/Community Addons/base_automation/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/base_automation/Frontend|Frontend]] (8 files)

## Key models

- `base.automation`
- `ir.actions.server`
- `ir.cron`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






