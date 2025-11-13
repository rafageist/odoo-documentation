<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Push notification to track listeners

- Version: v18
- Category: enterprise
- Source: enterprise18/website_event_track_social
- Dependencies: [[Odoo 18/Enterprise Addons/website_event_social/website_event_social|website_event_social]], [[Odoo 18/Community Addons/website_event_track/website_event_track|website_event_track]]

## Summary

Send reminder push notifications to event attendees based on favorites tracks.

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Track`
- `SocialPost`
- `website.visitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Push notification to track listeners - Models and Relations
class Track
class SocialPost
class "website.visitor" as website_visitor
class "social.post" as social_post
Track --|> social_post : one2many
class "event.track" as event_track
SocialPost --> event_track : many2one
website_visitor .. event_track : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
