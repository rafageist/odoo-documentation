
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Website Generator

- Scope: Enterprise Addons
- Source: enterprise/website_generator
- Dependencies: [[docs/Community Addons/website/website|website]], [[docs/Enterprise Addons/website_enterprise/website_enterprise|website_enterprise]]

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
!include ../../../templates/DiagramStyles.puml
title Website Generator - Models and Relations
class "website_generator.request" as website_generator_request
class WebsitePage
class Website
class website
website_generator_request --> website : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


