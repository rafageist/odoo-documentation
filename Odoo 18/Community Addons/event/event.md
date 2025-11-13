<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Events Organization

- Version: v18
- Category: community
- Source: odoo/addons/event
- Dependencies: [[Odoo 18/Community Addons/barcodes/barcodes|barcodes]], [[Odoo 18/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/phone_validation/phone_validation|phone_validation]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/utm/utm|utm]]

## Summary

Trainings, Conferences, Meetings, Exhibitions, Registrations

## XML Artifacts (detected)

- Views: 42
- Actions: 24
- Menus: 16
- Rules (ir.rule): 3
- Access CSV entries: 33

## Detected Models

- `event.type`
- `event.event`
- `event.type.mail`
- `event.mail`
- `event.mail.registration`
- `event.question`
- `event.question.answer`
- `event.registration`
- `event.registration.answer`
- `event.stage`
- `event.tag.category`
- `event.tag`
- `event.type.ticket`
- `event.event.ticket`
- `MailTemplate`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Events Organization - Models and Relations
class "event.type" as event_type
class "event.event" as event_event
class "event.type.mail" as event_type_mail
class "event.mail" as event_mail
class "event.mail.registration" as event_mail_registration
class "event.question" as event_question
class "event.question.answer" as event_question_answer
class "event.registration" as event_registration
class "event.registration.answer" as event_registration_answer
class "event.stage" as event_stage
class "event.tag.category" as event_tag_category
class "event.tag" as event_tag
class "event.type.ticket" as event_type_ticket
class "event.event.ticket" as event_event_ticket
class MailTemplate
class ResPartner
event_type --|> event_type_ticket : one2many
event_type .. event_tag : many2many
event_type --|> event_type_mail : one2many
event_type --|> event_question : one2many
class "res.users" as res_users
event_event --> res_users : many2one
class "res.company" as res_company
event_event --> res_company : many2one
class "res.partner" as res_partner
event_event --> res_partner : many2one
event_event --> event_type : many2one
event_event --|> event_mail : one2many
event_event .. event_tag : many2many
event_event --> event_stage : many2one
event_event --|> event_registration : one2many
event_event --|> event_event_ticket : one2many
event_event --> res_partner : many2one
event_event --> res_partner : many2one
class "res.country" as res_country
event_event --> res_country : many2one
event_event --|> event_question : one2many
event_event --|> event_question : one2many
event_event --|> event_question : one2many
event_type_mail --> event_type : many2one
event_mail --> event_event : many2one
event_mail --> event_registration : many2one
event_mail --|> event_mail_registration : one2many
event_mail_registration --> event_mail : many2one
event_mail_registration --> event_registration : many2one
event_question --> event_type : many2one
event_question --> event_event : many2one
event_question --|> event_question_answer : one2many
event_question_answer --> event_question : many2one
event_registration --> event_event : many2one
event_registration --> event_event_ticket : many2one
class "utm.campaign" as utm_campaign
event_registration --> utm_campaign : many2one
class "utm.source" as utm_source
event_registration --> utm_source : many2one
class "utm.medium" as utm_medium
event_registration --> utm_medium : many2one
event_registration --> res_partner : many2one
event_registration --> res_company : many2one
event_registration --|> event_registration_answer : one2many
event_registration --|> event_registration_answer : one2many
event_registration --|> event_mail_registration : one2many
event_registration_answer --> event_question : many2one
event_registration_answer --> event_registration : many2one
event_registration_answer --> res_partner : many2one
event_registration_answer --> event_event : many2one
event_registration_answer --> event_question_answer : many2one
event_tag_category --|> event_tag : one2many
event_tag --> event_tag_category : many2one
event_type_ticket --> event_type : many2one
event_event_ticket --> event_event : many2one
event_event_ticket --> res_company : many2one
event_event_ticket --|> event_registration : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
