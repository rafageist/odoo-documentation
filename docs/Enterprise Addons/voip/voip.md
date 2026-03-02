<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Phone

- Scope: Enterprise Addons
- Source: enterprise/voip
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]], [[docs/Community Addons/web/web|web]], [[docs/Enterprise Addons/web_mobile/web_mobile|web_mobile]]

## Summary

Make and receive phone calls from within Odoo.

## XML Artifacts (detected)

- Views: 12
- Actions: 3
- Menus: 5
- Rules (ir.rule): 4
- Access CSV entries: 6

## Detected Models

- `mail.activity`
- `ResCountry`
- `res.partner`
- `ResUsers`
- `ResUsersSettings`
- `voip.call`
- `voip.provider`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Phone - Models and Relations
class "mail.activity" as mail_activity
class ResCountry
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



