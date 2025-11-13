<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# OAuth2 Authentication

- Version: v18
- Category: community
- Source: odoo/addons/auth_oauth
- Dependencies: base (not documented), [[Odoo 18/Community Addons/web/web|web]], [[Odoo 18/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 18/Community Addons/auth_signup/auth_signup|auth_signup]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `auth.oauth.provider`
- `IrConfigParameter`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title OAuth2 Authentication - Models and Relations
class "auth.oauth.provider" as auth_oauth_provider
class IrConfigParameter
class ResUsers
ResUsers --> auth_oauth_provider : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
