<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Customer Rating

- Version: v18
- Category: community
- Source: odoo/addons/rating
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]]
## XML Artifacts (detected)

- Views: 10
- Actions: 3
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `MailMessage`
- `rating.rating`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Customer Rating - Models and Relations
class MailMessage
class "rating.rating" as rating_rating
MailMessage --|> rating_rating : one2many
MailMessage --> rating_rating : many2one
class "ir.model" as ir_model
rating_rating --> ir_model : many2one
rating_rating --> ir_model : many2one
class "res.partner" as res_partner
rating_rating --> res_partner : many2one
rating_rating --> res_partner : many2one
class "mail.message" as mail_message
rating_rating --> mail_message : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
