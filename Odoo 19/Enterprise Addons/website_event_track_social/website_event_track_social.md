<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Push notification to track listeners

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/website_event_track_social
- Dependencies: [[Odoo 19/Enterprise Addons/website_event_social/website_event_social|website_event_social]], [[Odoo 19/Community Addons/website_event_track/website_event_track|website_event_track]]

## Summary

Send reminder push notifications to event attendees based on favorites tracks.

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `EventTrack`
- `SocialPost`
- `WebsiteVisitor`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Push notification to track listeners - Models and Relations
class EventTrack
class SocialPost
class WebsiteVisitor
class "social.post" as social_post
EventTrack --|> social_post : one2many
class "event.track" as event_track
SocialPost --> event_track : many2one
WebsiteVisitor .. event_track : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

