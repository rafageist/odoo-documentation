<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Social X

- Version: v18
- Category: enterprise
- Source: enterprise18/social_twitter
- Dependencies: [[Odoo 18/Enterprise Addons/social/social|social]], [[Odoo 18/Community Addons/iap/iap|iap]]

## Summary

Manage your X accounts and schedule posts

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `SocialAccountTwitter`
- `SocialLivePostTwitter`
- `SocialMediaTwitter`
- `SocialPostTwitter`
- `SocialPostTemplate`
- `SocialStreamTwitter`
- `SocialStreamPostTwitter`
- `social.twitter.account`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Social X - Models and Relations
class SocialAccountTwitter
class SocialLivePostTwitter
class SocialMediaTwitter
class SocialPostTwitter
class SocialPostTemplate
class SocialStreamTwitter
class SocialStreamPostTwitter
class "social.twitter.account" as social_twitter_account
class "ir.attachment" as ir_attachment
SocialPostTemplate .. ir_attachment : many2many
SocialStreamTwitter --> social_twitter_account : many2one
class "social.account" as social_account
social_twitter_account --> social_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
