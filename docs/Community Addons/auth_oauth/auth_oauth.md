<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# OAuth2 Authentication

- Scope: Community Addons
- Source: odoo/addons/auth_oauth
- Dependencies: base (not documented), [[docs/Community Addons/web/web|web]], [[docs/Community Addons/base_setup/base_setup|base_setup]], [[docs/Community Addons/auth_signup/auth_signup|auth_signup]]

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
!include ../../../templates/DiagramStyles.puml
title OAuth2 Authentication - Models and Relations
class "auth.oauth.provider" as auth_oauth_provider
class IrConfig_Parameter
class ResUsers
ResUsers --> auth_oauth_provider : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





