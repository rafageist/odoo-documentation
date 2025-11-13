<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Social Instagram

- Version: v18
- Category: enterprise
- Source: enterprise18/social_instagram
- Dependencies: [[Odoo 18/Enterprise Addons/social/social|social]]

## Summary

Manage your Instagram Business accounts and schedule posts

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SocialAccountInstagram`
- `SocialLivePostInstagram`
- `SocialMediaInstagram`
- `SocialPostInstagram`
- `SocialPostTemplate`
- `SocialStreamInstagram`
- `SocialStreamPostInstagram`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Social Instagram - Models and Relations
class SocialAccountInstagram
class SocialLivePostInstagram
class SocialMediaInstagram
class SocialPostInstagram
class SocialPostTemplate
class SocialStreamInstagram
class SocialStreamPostInstagram
class "ir.attachment" as ir_attachment
SocialPostTemplate .. ir_attachment : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
