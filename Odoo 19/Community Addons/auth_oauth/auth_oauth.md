<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# OAuth2 Authentication

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/auth_oauth
- Dependencies: base (not documented), [[Odoo 19/Community Addons/web/web|web]], [[Odoo 19/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 19/Community Addons/auth_signup/auth_signup|auth_signup]]

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `auth.oauth.provider`
- `IrConfig_Parameter`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title OAuth2 Authentication - Models and Relations
class "auth.oauth.provider" as auth_oauth_provider
class IrConfig_Parameter
class ResUsers
ResUsers --> auth_oauth_provider : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


