<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Mail Plugin

- Version: v19
- Category: community
- Source: odoo19/addons/mail_plugin
- Dependencies: [[Odoo 19/Community Addons/web/web|web]], [[Odoo 19/Community Addons/contacts/contacts|contacts]], [[Odoo 19/Community Addons/iap/iap|iap]]

## Summary

Allows integration with mail plugins.

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `ResPartner`
- `res.partner.iap`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mail Plugin - Models and Relations
class ResPartner
class "res.partner.iap" as res_partner_iap
class "res.partner" as res_partner
res_partner_iap --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
