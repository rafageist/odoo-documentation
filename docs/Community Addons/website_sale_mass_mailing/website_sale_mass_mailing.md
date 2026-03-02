<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Checkout Newsletter

- Scope: Community Addons
- Source: odoo/addons/website_sale_mass_mailing
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]], [[docs/Community Addons/website_mass_mailing/website_mass_mailing|website_mass_mailing]]

## Summary

Let new customers sign up for a newsletter during checkout

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Website`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Checkout Newsletter - Models and Relations
class Website
class "mailing.list" as mailing_list
Website --> mailing_list : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



