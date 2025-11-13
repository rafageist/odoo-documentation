<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Social X

- Version: v19
- Category: enterprise
- Source: enterprise19/social_twitter
- Dependencies: [[Odoo 19/Enterprise Addons/social/social|social]], [[Odoo 19/Community Addons/iap/iap|iap]]

## Summary

Manage your X accounts and schedule posts

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `SocialAccount`
- `SocialLivePost`
- `SocialMedia`
- `SocialPost`
- `SocialPostTemplate`
- `SocialStream`
- `SocialStreamPost`
- `social.twitter.account`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Social X - Models and Relations
class SocialAccount
class SocialLivePost
class SocialMedia
class SocialPost
class SocialPostTemplate
class SocialStream
class SocialStreamPost
class "social.twitter.account" as social_twitter_account
class "ir.attachment" as ir_attachment
SocialPostTemplate .. ir_attachment : many2many
SocialStream --> social_twitter_account : many2one
class "social.account" as social_account
social_twitter_account --> social_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
