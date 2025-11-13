<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Advanced Events

- Version: v18
- Category: community
- Source: odoo/addons/website_event_track
- Dependencies: [[Odoo 18/Community Addons/website_event/website_event|website_event]]

## Summary

Sponsors, Tracks, Agenda, Event News

## XML Artifacts (detected)

- Views: 26
- Actions: 9
- Menus: 6
- Rules (ir.rule): 2
- Access CSV entries: 19

## Detected Models

- `Event`
- `event.track`
- `event.track.location`
- `event.track.stage`
- `event.track.tag`
- `event.track.tag.category`
- `event.track.visitor`
- `EventType`
- `Website`
- `EventMenu`
- `WebsiteMenu`
- `website.visitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Advanced Events - Models and Relations
class Event
class "event.track" as event_track
class "event.track.location" as event_track_location
class "event.track.stage" as event_track_stage
class "event.track.tag" as event_track_tag
class "event.track.tag.category" as event_track_tag_category
class "event.track.visitor" as event_track_visitor
class EventType
class Website
class EventMenu
class WebsiteMenu
class "website.visitor" as website_visitor
Event --|> event_track : one2many
class "website.event.menu" as website_event_menu
Event --|> website_event_menu : one2many
Event --|> website_event_menu : one2many
Event .. event_track_tag : many2many
Event .. event_track_tag : many2many
class "event.event" as event_event
event_track --> event_event : many2one
class "res.users" as res_users
event_track --> res_users : many2one
class "res.company" as res_company
event_track --> res_company : many2one
event_track .. event_track_tag : many2many
event_track --> event_track_stage : many2one
class "res.partner" as res_partner
event_track --> res_partner : many2one
event_track --> event_track_location : many2one
event_track --|> event_track_visitor : one2many
event_track .. website_visitor : many2many
class "mail.template" as mail_template
event_track_stage --> mail_template : many2one
event_track_tag .. event_track : many2many
event_track_tag --> event_track_tag_category : many2one
event_track_tag_category --|> event_track_tag : one2many
event_track_visitor --> res_partner : many2one
event_track_visitor --> website_visitor : many2one
event_track_visitor --> event_track : many2one
website_visitor --|> event_track_visitor : one2many
website_visitor .. event_track : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
