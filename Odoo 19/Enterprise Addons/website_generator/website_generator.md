<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Website Generator

- Version: v19
- Category: enterprise
- Source: enterprise19/website_generator
- Dependencies: [[Odoo 19/Community Addons/website/website|website]], [[Odoo 19/Enterprise Addons/website_enterprise/website_enterprise|website_enterprise]]

## Summary

Import a pre-existing website

## XML Artifacts (detected)

- Views: 0
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `website_generator.request`
- `WebsitePage`
- `Website`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Generator - Models and Relations
class "website_generator.request" as website_generator_request
class WebsitePage
class Website
class website
website_generator_request --> website : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
