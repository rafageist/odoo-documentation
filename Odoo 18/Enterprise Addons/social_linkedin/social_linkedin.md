<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Social LinkedIn

- Version: v18
- Category: enterprise
- Source: enterprise18/social_linkedin
- Dependencies: [[Odoo 18/Enterprise Addons/social/social|social]], [[Odoo 18/Community Addons/iap/iap|iap]]

## Summary

Manage your LinkedIn accounts and schedule posts

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SocialAccountLinkedin`
- `SocialLivePostLinkedin`
- `SocialMediaLinkedin`
- `SocialPostLinkedin`
- `SocialPostTemplate`
- `SocialStreamLinkedIn`
- `SocialStreamPostLinkedIn`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Social LinkedIn - Models and Relations
class SocialAccountLinkedin
class SocialLivePostLinkedin
class SocialMediaLinkedin
class SocialPostLinkedin
class SocialPostTemplate
class SocialStreamLinkedIn
class SocialStreamPostLinkedIn
class "ir.attachment" as ir_attachment
SocialPostTemplate .. ir_attachment : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
