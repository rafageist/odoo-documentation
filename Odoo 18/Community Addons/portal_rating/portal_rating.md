<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Portal Rating

- Version: v18
- Category: community
- Source: odoo/addons/portal_rating
- Dependencies: [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/rating/rating|rating]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MailMessage`
- `Rating`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Portal Rating - Models and Relations
class MailMessage
class Rating
class "res.partner" as res_partner
Rating --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
