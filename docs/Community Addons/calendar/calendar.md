<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Calendar

- Scope: Community Addons
- Source: odoo/addons/calendar
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]]

## Summary

Schedule employees' meetings

## XML Artifacts (detected)

- Views: 18
- Actions: 8
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
- `DiscussChannel`
- `MailActivity`
- `MailActivityType`
- `ResPartner`
- `ResUsers`
- `ResUsersSettings`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Calendar - Models and Relations
class "calendar.alarm" as calendar_alarm
class "calendar.attendee" as calendar_attendee
class "calendar.event" as calendar_event
class "calendar.event.type" as calendar_event_type
class "calendar.filters" as calendar_filters
class "calendar.recurrence" as calendar_recurrence
class DiscussChannel
class MailActivity
class MailActivityType
class ResPartner
class ResUsers
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
calendar_event .. res_partner : many2many
calendar_event .. calendar_alarm : many2many
calendar_event --> calendar_recurrence : many2one
calendar_filters --> res_users : many2one
calendar_filters --> res_partner : many2one
calendar_recurrence --> calendar_event : many2one
calendar_recurrence --|> calendar_event : one2many
class "ir.cron.trigger" as ir_cron_trigger
calendar_recurrence --> ir_cron_trigger : many2one
DiscussChannel --|> calendar_event : one2many
MailActivity --> calendar_event : many2one
ResPartner .. calendar_event : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





