<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# VoIP

- Version: v18
- Category: enterprise
- Source: enterprise18/voip
- Dependencies: base (not documented), [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/phone_validation/phone_validation|phone_validation]], [[Odoo 18/Community Addons/web/web|web]], [[Odoo 18/Enterprise Addons/web_mobile/web_mobile|web_mobile]]

## Summary

Make and receive phone calls from within Odoo.

## XML Artifacts (detected)

- Views: 7
- Actions: 2
- Menus: 2
- Rules (ir.rule): 2
- Access CSV entries: 4

## Detected Models

- `MailActivity`
- `res.partner`
- `ResUsers`
- `ResUsersSettings`
- `voip.call`
- `voip.provider`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title VoIP - Models and Relations
class MailActivity
class "res.partner" as res_partner
class ResUsers
class ResUsersSettings
class "voip.call" as voip_call
class "voip.provider" as voip_provider
ResUsers --> voip_call : many2one
ResUsers --> voip_provider : many2one
ResUsersSettings --> voip_provider : many2one
voip_call --> res_partner : many2one
class "res.users" as res_users
voip_call --> res_users : many2one
class "res.company" as res_company
voip_provider --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
