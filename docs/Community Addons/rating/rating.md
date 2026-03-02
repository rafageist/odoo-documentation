<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Customer Rating

- Scope: Community Addons
- Source: odoo/addons/rating
- Dependencies: [[docs/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 9
- Actions: 3
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `MailMessage`
- `rating.rating`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





