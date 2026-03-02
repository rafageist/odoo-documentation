<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Marketing Card

- Scope: Community Addons
- Source: odoo/addons/marketing_card
- Dependencies: [[docs/Community Addons/link_tracker/link_tracker|link_tracker]], [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[docs/Community Addons/website/website|website]]

## Summary

Generate dynamic shareable cards

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 6
- Views: 8
- Actions: 3
- Menus: 4
- Rules (ir.rule): 2
- Access CSV entries: 9
- Controller units: 1
- Frontend asset files: 0

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
title Marketing Card - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n8 views\n6 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n2 rules\n9 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/marketing_card/Models|Models]] (8)
- Views and XML: [[docs/Community Addons/marketing_card/Views|Views]] (6 files)
- Controllers: [[docs/Community Addons/marketing_card/Controllers|Controllers]] (1)

## Key models

- `card.campaign`
- `card.campaign.tag`
- `card.card`
- `card.template`
- `ir.model`
- `mail.compose.message`
- `mailing.mailing`
- `utm.source`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






