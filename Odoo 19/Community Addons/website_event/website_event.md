<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Events

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_event
- Dependencies: [[Odoo 19/Community Addons/event/event|event]], [[Odoo 19/Community Addons/website/website|website]], [[Odoo 19/Community Addons/website_partner/website_partner|website_partner]], [[Odoo 19/Community Addons/website_mail/website_mail|website_mail]], [[Odoo 19/Community Addons/html_builder/html_builder|html_builder]]

## Summary

Publish events, sell tickets

## XML Artifacts (detected)

- Views: 19
- Actions: 6
- Menus: 2
- Rules (ir.rule): 8
- Access CSV entries: 27

## Detected Models

- `event.event`
- `EventRegistration`
- `event.tag`
- `event.tag.category`
- `EventType`
- `Website`
- `website.event.menu`
- `WebsiteMenu`
- `WebsiteSnippetFilter`
- `WebsiteVisitor`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Events - Models and Relations
class "event.event" as event_event
class EventRegistration
class "event.tag" as event_tag
class "event.tag.category" as event_tag_category
class EventType
class Website
class "website.event.menu" as website_event_menu
class WebsiteMenu
class WebsiteSnippetFilter
class WebsiteVisitor
class "website.menu" as website_menu
event_event --> website_menu : many2one
event_event --|> website_event_menu : one2many
event_event --|> website_event_menu : one2many
event_event --|> website_event_menu : one2many
event_event --|> website_event_menu : one2many
class "website.visitor" as website_visitor
EventRegistration --> website_visitor : many2one
website_event_menu --> website_menu : many2one
website_event_menu --> event_event : many2one
class "ir.ui.view" as ir_ui_view
website_event_menu --> ir_ui_view : many2one
class "event.registration" as event_registration
WebsiteVisitor --|> event_registration : one2many
WebsiteVisitor .. event_event : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

