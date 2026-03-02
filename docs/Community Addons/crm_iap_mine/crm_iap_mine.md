<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Lead Generation

- Scope: Community Addons
- Source: odoo/addons/crm_iap_mine
- Dependencies: [[docs/Community Addons/iap_crm/iap_crm|iap_crm]], [[docs/Community Addons/iap_mail/iap_mail|iap_mail]]

## Summary

Generate Leads/Opportunities based on country, industries, size, etc.

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 4
- Views: 8
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 5
- Controller units: 0
- Frontend asset files: 1

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
title Lead Generation - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n8 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/crm_iap_mine/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/crm_iap_mine/Views|Views]] (4 files)
- Frontend: [[docs/Community Addons/crm_iap_mine/Frontend|Frontend]] (1 files)

## Key models

- `crm.iap.lead.helpers`
- `crm.iap.lead.industry`
- `crm.iap.lead.mining.request`
- `crm.iap.lead.role`
- `crm.iap.lead.seniority`
- `crm.lead`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






