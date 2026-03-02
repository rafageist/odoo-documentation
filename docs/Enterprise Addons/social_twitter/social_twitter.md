<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Social X

- Scope: Enterprise Addons
- Source: enterprise/social_twitter
- Dependencies: [[docs/Enterprise Addons/social/social|social]], [[docs/Community Addons/iap/iap|iap]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



