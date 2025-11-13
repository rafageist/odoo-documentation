<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Phone - CRM

- Version: v19
- Category: enterprise
- Source: enterprise19/voip_crm
- Dependencies: [[Odoo 19/Community Addons/crm/crm|crm]], [[Odoo 19/Enterprise Addons/voip/voip|voip]]

## Summary

Phone integration with CRM module.

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 0

## Detected Models

- `crm.lead`
- `res.partner`
- `VoipCall`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Phone - CRM - Models and Relations
class "crm.lead" as crm_lead
class "res.partner" as res_partner
class VoipCall
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
