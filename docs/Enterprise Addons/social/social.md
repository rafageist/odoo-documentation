<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Social Marketing

- Scope: Enterprise Addons
- Source: enterprise/social
- Dependencies: [[docs/Community Addons/web/web|web]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/iap/iap|iap]], [[docs/Community Addons/link_tracker/link_tracker|link_tracker]]

## Summary

Manage your social media and website visitors

## XML Artifacts (detected)

- Views: 23
- Actions: 8
- Menus: 15
- Rules (ir.rule): 12
- Access CSV entries: 21

## Detected Models

- `social.account`
- `social.live.post`
- `social.media`
- `social.post`
- `social.post.template`
- `social.stream`
- `social.stream.post`
- `social.stream.post.image`
- `social.stream.type`
- `UtmCampaign`
- `UtmMedium`
- `UtmSource`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Social Marketing - Models and Relations
class "social.account" as social_account
class "social.live.post" as social_live_post
class "social.media" as social_media
class "social.post" as social_post
class "social.post.template" as social_post_template
class "social.stream" as social_stream
class "social.stream.post" as social_stream_post
class "social.stream.post.image" as social_stream_post_image
class "social.stream.type" as social_stream_type
class UtmCampaign
class UtmMedium
class UtmSource
social_account --> social_media : many2one
class "utm.medium" as utm_medium
social_account --> utm_medium : many2one
class "res.company" as res_company
social_account --> res_company : many2one
social_live_post --> social_post : many2one
social_live_post --> social_account : many2one
class "ir.attachment" as ir_attachment
social_live_post .. ir_attachment : many2many
social_live_post --> res_company : many2one
social_media --|> social_account : one2many
social_media --|> social_stream_type : one2many
social_post .. social_account : many2many
social_post --> res_company : many2one
social_post .. social_media : many2many
social_post --|> social_live_post : one2many
class "utm.campaign" as utm_campaign
social_post --> utm_campaign : many2one
social_post_template .. ir_attachment : many2many
social_post_template .. social_account : many2many
social_stream --> social_media : many2one
social_stream --> social_account : many2one
social_stream --> social_stream_type : many2one
social_stream --|> social_stream_post : one2many
social_stream --> res_company : many2one
social_stream_post --> social_stream : many2one
social_stream_post --> res_company : many2one
social_stream_post --|> social_stream_post_image : one2many
social_stream_post_image --> social_stream_post : many2one
social_stream_type --> social_media : many2one
UtmCampaign --|> social_post : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



