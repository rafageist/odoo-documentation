<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Calendar

- Version: v18
- Category: community
- Source: odoo/addons/calendar
- Dependencies: base (not documented), [[Odoo 18/Community Addons/mail/mail|mail]]

## Summary

Schedule employees' meetings

## XML Artifacts (detected)

- Views: 18
- Actions: 7
- Menus: 8
- Rules (ir.rule): 4
- Access CSV entries: 15

## Detected Models

- `calendar.alarm`
- `calendar.attendee`
- `calendar.event`
- `calendar.event.type`
- `calendar.filters`
- `calendar.recurrence`
- `MailActivity`
- `MailActivityType`
- `Partner`
- `Users`
- `ResUsersSettings`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Calendar - Models and Relations
class "calendar.alarm" as calendar_alarm
class "calendar.attendee" as calendar_attendee
class "calendar.event" as calendar_event
class "calendar.event.type" as calendar_event_type
class "calendar.filters" as calendar_filters
class "calendar.recurrence" as calendar_recurrence
class MailActivity
class MailActivityType
class Partner
class Users
class ResUsersSettings
class "mail.template" as mail_template
calendar_alarm --> mail_template : many2one
calendar_attendee --> calendar_event : many2one
calendar_attendee --> calendar_recurrence : many2one
class "res.partner" as res_partner
calendar_attendee --> res_partner : many2one
class "res.users" as res_users
calendar_event --> res_users : many2one
calendar_event --> res_partner : many2one
class "discuss.channel" as discuss_channel
calendar_event --> discuss_channel : many2one
calendar_event .. calendar_event_type : many2many
class "ir.model" as ir_model
calendar_event --> ir_model : many2one
class "mail.activity" as mail_activity
calendar_event --|> mail_activity : one2many
calendar_event --|> calendar_attendee : one2many
calendar_event --> calendar_attendee : many2one
calendar_event .. res_partner : many2many
calendar_event .. res_partner : many2many
calendar_event .. calendar_alarm : many2many
calendar_event --> calendar_recurrence : many2one
calendar_filters --> res_users : many2one
calendar_filters --> res_partner : many2one
calendar_recurrence --> calendar_event : many2one
calendar_recurrence --|> calendar_event : one2many
class "ir.cron.trigger" as ir_cron_trigger
calendar_recurrence --> ir_cron_trigger : many2one
MailActivity --> calendar_event : many2one
Partner .. calendar_event : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
