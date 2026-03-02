<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Certificate

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/certificate
- Dependencies: [[Odoo 19/Community Addons/base_setup/base_setup|base_setup]]

## Summary

Manage certificate

## XML Artifacts (detected)

- Views: 7
- Actions: 2
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `certificate.certificate`
- `certificate.key`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Certificate - Models and Relations
class "certificate.certificate" as certificate_certificate
class "certificate.key" as certificate_key
certificate_certificate --> certificate_key : many2one
certificate_certificate --> certificate_key : many2one
class "res.company" as res_company
certificate_certificate --> res_company : many2one
certificate_key --> res_company : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


