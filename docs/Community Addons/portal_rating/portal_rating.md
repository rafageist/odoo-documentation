<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Portal Rating

- Scope: Community Addons
- Source: odoo/addons/portal_rating
- Dependencies: [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/rating/rating|rating]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MailMessage`
- `RatingRating`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Portal Rating - Models and Relations
class MailMessage
class RatingRating
class "res.partner" as res_partner
RatingRating --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





