<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Phone

- Version: v19
- Category: enterprise
- Source: enterprise19/voip
- Dependencies: base (not documented), [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/phone_validation/phone_validation|phone_validation]], [[Odoo 19/Community Addons/web/web|web]], [[Odoo 19/Enterprise Addons/web_mobile/web_mobile|web_mobile]]

## Summary

Make and receive phone calls from within Odoo.

## XML Artifacts (detected)

- Views: 12
- Actions: 3
- Menus: 5
- Rules (ir.rule): 4
- Access CSV entries: 5

## Detected Models

- `mail.activity`
- `res.partner`
- `ResUsers`
- `ResUsersSettings`
- `voip.call`
- `voip.provider`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Phone - Models and Relations
class "mail.activity" as mail_activity
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
class "res.country" as res_country
voip_call --> res_country : many2one
class "res.company" as res_company
voip_provider --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
