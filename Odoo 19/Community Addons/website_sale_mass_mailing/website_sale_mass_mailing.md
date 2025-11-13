<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Checkout Newsletter

- Version: v19
- Category: community
- Source: odoo19/addons/website_sale_mass_mailing
- Dependencies: [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]], [[Odoo 19/Community Addons/website_mass_mailing/website_mass_mailing|website_mass_mailing]]

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
!include ../../../Templates/DiagramStyles.puml
title Checkout Newsletter - Models and Relations
class Website
class "mailing.list" as mailing_list
Website --> mailing_list : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
