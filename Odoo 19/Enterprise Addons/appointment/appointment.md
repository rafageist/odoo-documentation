<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Appointments

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/appointment
- Dependencies: [[Odoo 19/Community Addons/calendar/calendar|calendar]], [[Odoo 19/Community Addons/phone_validation/phone_validation|phone_validation]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Community Addons/resource/resource|resource]], [[Odoo 19/Enterprise Addons/web_gantt/web_gantt|web_gantt]]

## Summary

Allow people to book meetings in your agenda

## XML Artifacts (detected)

- Views: 38
- Actions: 14
- Menus: 16
- Rules (ir.rule): 13
- Access CSV entries: 29

## Detected Models

- `appointment.answer`
- `appointment.answer.input`
- `appointment.booking.line`
- `appointment.invite`
- `appointment.question`
- `appointment.resource`
- `appointment.slot`
- `appointment.type`
- `CalendarAlarm`
- `CalendarAttendee`
- `CalendarEvent`
- `ResPartner`
- `AppointmentType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Appointments - Models and Relations
class "appointment.answer" as appointment_answer
class "appointment.answer.input" as appointment_answer_input
class "appointment.booking.line" as appointment_booking_line
class "appointment.invite" as appointment_invite
class "appointment.question" as appointment_question
class "appointment.resource" as appointment_resource
class "appointment.slot" as appointment_slot
class "appointment.type" as appointment_type
class CalendarAlarm
class CalendarAttendee
class CalendarEvent
class ResPartner
class AppointmentType
appointment_answer --> appointment_question : many2one
appointment_answer_input --> appointment_question : many2one
appointment_answer_input --> appointment_answer : many2one
appointment_answer_input --> appointment_type : many2one
class "calendar.event" as calendar_event
appointment_answer_input --> calendar_event : many2one
class "res.partner" as res_partner
appointment_answer_input --> res_partner : many2one
appointment_booking_line --> appointment_resource : many2one
class "res.users" as res_users
appointment_booking_line --> res_users : many2one
appointment_booking_line --> appointment_type : many2one
appointment_booking_line --> calendar_event : many2one
appointment_invite --> appointment_invite : many2one
appointment_invite .. appointment_type : many2many
appointment_invite .. appointment_resource : many2many
appointment_invite .. res_users : many2many
appointment_invite .. appointment_resource : many2many
appointment_invite .. res_users : many2many
appointment_invite --|> calendar_event : one2many
appointment_question .. appointment_type : many2many
appointment_question --|> appointment_answer : one2many
appointment_question --|> appointment_answer_input : one2many
appointment_resource .. appointment_resource : many2many
appointment_resource .. appointment_resource : many2many
appointment_resource .. appointment_resource : many2many
appointment_resource .. appointment_type : many2many
appointment_slot --> appointment_type : many2one
appointment_slot .. res_users : many2many
appointment_slot .. appointment_resource : many2many
appointment_type --> res_partner : many2one
class "mail.template" as mail_template
appointment_type --> mail_template : many2one
appointment_type --> mail_template : many2one
class "res.country" as res_country
appointment_type .. res_country : many2many
appointment_type .. appointment_question : many2many
class "calendar.alarm" as calendar_alarm
appointment_type .. calendar_alarm : many2many
appointment_type --|> appointment_slot : one2many
appointment_type .. res_users : many2many
appointment_type .. appointment_resource : many2many
appointment_type .. appointment_invite : many2many
appointment_type --|> calendar_event : one2many
CalendarEvent --|> appointment_answer_input : one2many
CalendarEvent --> appointment_type : many2one
CalendarEvent --> appointment_invite : many2one
CalendarEvent .. appointment_resource : many2many
CalendarEvent .. appointment_resource : many2many
CalendarEvent --|> appointment_booking_line : one2many
CalendarEvent .. res_partner : many2many
CalendarEvent --> res_users : many2one
CalendarEvent --> res_partner : many2one
CalendarEvent .. appointment_resource : many2many
ResPartner .. calendar_event : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

