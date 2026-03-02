<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Mail Plugin

- Scope: Community Addons
- Source: odoo/addons/mail_plugin
- Dependencies: [[docs/Community Addons/web/web|web]], [[docs/Community Addons/contacts/contacts|contacts]], [[docs/Community Addons/iap/iap|iap]]

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
!include ../../../templates/DiagramStyles.puml
title Mail Plugin - Models and Relations
class ResPartner
class "res.partner.iap" as res_partner_iap
class "res.partner" as res_partner
res_partner_iap --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





