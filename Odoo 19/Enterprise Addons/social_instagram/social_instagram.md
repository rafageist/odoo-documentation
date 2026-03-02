<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Social Instagram

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/social_instagram
- Dependencies: [[Odoo 19/Enterprise Addons/social/social|social]]

## Summary

Manage your Instagram Business accounts and schedule posts

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
!include ../../../Templates/DiagramStyles.puml
title Social Instagram - Models and Relations
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

