<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Social Facebook

- Version: v18
- Category: enterprise
- Source: enterprise18/social_facebook
- Dependencies: [[Odoo 18/Enterprise Addons/social/social|social]]

## Summary

Manage your Facebook pages and schedule posts

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SocialAccountFacebook`
- `SocialLivePostFacebook`
- `SocialMediaFacebook`
- `SocialPostFacebook`
- `SocialPostTemplate`
- `SocialStreamFacebook`
- `SocialStreamPostFacebook`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Social Facebook - Models and Relations
class SocialAccountFacebook
class SocialLivePostFacebook
class SocialMediaFacebook
class SocialPostFacebook
class SocialPostTemplate
class SocialStreamFacebook
class SocialStreamPostFacebook
class "ir.attachment" as ir_attachment
SocialPostTemplate .. ir_attachment : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
