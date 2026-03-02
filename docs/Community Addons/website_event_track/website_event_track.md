
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Advanced Events

- Scope: Community Addons
- Source: odoo/addons/website_event_track
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]]

## Summary

Sponsors, Tracks, Agenda, Event News

## XML Artifacts (detected)

- Views: 26
- Actions: 9
- Menus: 6
- Rules (ir.rule): 2
- Access CSV entries: 19

## Detected Models

- `EventEvent`
- `event.track`
- `event.track.location`
- `event.track.stage`
- `event.track.tag`
- `event.track.tag.category`
- `event.track.visitor`
- `EventType`
- `Website`
- `WebsiteEventMenu`
- `WebsiteMenu`
- `WebsiteVisitor`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Advanced Events - Models and Relations
class EventEvent
class "event.track" as event_track
class "event.track.location" as event_track_location
class "event.track.stage" as event_track_stage
class "event.track.tag" as event_track_tag
class "event.track.tag.category" as event_track_tag_category
class "event.track.visitor" as event_track_visitor
class EventType
class Website
class WebsiteEventMenu
class WebsiteMenu
class WebsiteVisitor
EventEvent --|> event_track : one2many
class "website.event.menu" as website_event_menu
EventEvent --|> website_event_menu : one2many
EventEvent --|> website_event_menu : one2many
EventEvent .. event_track_tag : many2many
EventEvent .. event_track_tag : many2many
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
class "website.visitor" as website_visitor
event_track .. website_visitor : many2many
class "mail.template" as mail_template
event_track_stage --> mail_template : many2one
event_track_tag .. event_track : many2many
event_track_tag --> event_track_tag_category : many2one
event_track_tag_category --|> event_track_tag : one2many
event_track_visitor --> res_partner : many2one
event_track_visitor --> website_visitor : many2one
event_track_visitor --> event_track : many2one
WebsiteVisitor --|> event_track_visitor : one2many
WebsiteVisitor .. event_track : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

