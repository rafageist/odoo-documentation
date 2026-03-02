<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Phone - CRM

- Scope: Enterprise Addons
- Source: enterprise/voip_crm
- Dependencies: [[docs/Community Addons/crm/crm|crm]], [[docs/Enterprise Addons/voip/voip|voip]]

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
!include ../../../templates/DiagramStyles.puml
title Phone - CRM - Models and Relations
class "crm.lead" as crm_lead
class "res.partner" as res_partner
class VoipCall
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




