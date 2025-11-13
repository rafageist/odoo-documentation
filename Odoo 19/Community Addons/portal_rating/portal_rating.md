<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Portal Rating

- Version: v19
- Category: community
- Source: odoo19/addons/portal_rating
- Dependencies: [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Community Addons/rating/rating|rating]]
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
!include ../../../Templates/DiagramStyles.puml
title Portal Rating - Models and Relations
class MailMessage
class RatingRating
class "res.partner" as res_partner
RatingRating --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
