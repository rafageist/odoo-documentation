<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Blog

- Scope: Community Addons
- Source: odoo/addons/website_blog
- Dependencies: [[docs/Community Addons/website_mail/website_mail|website_mail]], [[docs/Community Addons/website_partner/website_partner|website_partner]], [[docs/Community Addons/html_builder/html_builder|html_builder]]

## Summary

Publish blog posts, announces, news

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 5
- Views: 12
- Actions: 7
- Menus: 5
- Rules (ir.rule): 2
- Access CSV entries: 16
- Controller units: 1
- Frontend asset files: 18

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
title Blog - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n12 views\n5 files" as views
component "Controllers\n4 routes" as controllers
component "Frontend\n18 files" as frontend
component "Security / Data\n2 rules\n16 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_blog/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/website_blog/Views|Views]] (5 files)
- Controllers: [[docs/Community Addons/website_blog/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_blog/Frontend|Frontend]] (18 files)

## Key models

- `blog.blog`
- `blog.post`
- `blog.tag`
- `blog.tag.category`
- `website`
- `website.snippet.filter`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





