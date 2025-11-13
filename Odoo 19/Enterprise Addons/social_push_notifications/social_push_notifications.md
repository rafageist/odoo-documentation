<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Social Push Notifications

- Version: v19
- Category: enterprise
- Source: enterprise19/social_push_notifications
- Dependencies: [[Odoo 19/Enterprise Addons/social/social|social]], [[Odoo 19/Community Addons/website/website|website]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
