<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Social Push Notifications

- Scope: Enterprise Addons
- Source: enterprise/social_push_notifications
- Dependencies: [[docs/Enterprise Addons/social/social|social]], [[docs/Community Addons/website/website|website]]

## Summary

Send live notifications to your web visitors

## XML Artifacts (detected)

- Views: 9
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `SocialAccount`
- `SocialLivePost`
- `SocialMedia`
- `SocialPost`
- `SocialPostTemplate`
- `UtmCampaign`
- `Website`
- `WebsiteVisitor`
- `website.visitor.push.subscription`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Social Push Notifications - Models and Relations
class SocialAccount
class SocialLivePost
class SocialMedia
class SocialPost
class SocialPostTemplate
class UtmCampaign
class Website
class WebsiteVisitor
class "website.visitor.push.subscription" as website_visitor_push_subscription
class website
SocialAccount --> website : many2one
class "website.visitor" as website_visitor
SocialLivePost .. website_visitor : many2many
class "social.post" as social_post
UtmCampaign --|> social_post : one2many
WebsiteVisitor --|> website_visitor_push_subscription : one2many
website_visitor_push_subscription --> website_visitor : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



