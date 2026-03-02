<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Social Facebook

- Scope: Enterprise Addons
- Source: enterprise/social_facebook
- Dependencies: [[docs/Enterprise Addons/social/social|social]]

## Summary

Manage your Facebook pages and schedule posts

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SocialAccount`
- `SocialLivePost`
- `SocialMedia`
- `SocialPost`
- `SocialPostTemplate`
- `SocialStream`
- `SocialStreamPost`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Social Facebook - Models and Relations
class SocialAccount
class SocialLivePost
class SocialMedia
class SocialPost
class SocialPostTemplate
class SocialStream
class SocialStreamPost
class "ir.attachment" as ir_attachment
SocialPostTemplate .. ir_attachment : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



