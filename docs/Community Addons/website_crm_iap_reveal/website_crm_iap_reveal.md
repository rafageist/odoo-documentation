<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Lead Generation From Website Visits

- Scope: Community Addons
- Source: odoo/addons/website_crm_iap_reveal
- Dependencies: [[docs/Community Addons/iap_crm/iap_crm|iap_crm]], [[docs/Community Addons/iap_mail/iap_mail|iap_mail]], [[docs/Community Addons/crm_iap_mine/crm_iap_mine|crm_iap_mine]], [[docs/Community Addons/website_crm/website_crm|website_crm]]

## Summary

Generate Leads/Opportunities from your website's traffic

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 5
- Views: 14
- Actions: 2
- Menus: 2
- Rules (ir.rule): 4
- Access CSV entries: 4
- Controller units: 0
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
title Lead Generation From Website Visits - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n14 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n4 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_crm_iap_reveal/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/website_crm_iap_reveal/Views|Views]] (5 files)

## Key models

- `crm.lead`
- `crm.reveal.rule`
- `crm.reveal.view`
- `ir.http`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




