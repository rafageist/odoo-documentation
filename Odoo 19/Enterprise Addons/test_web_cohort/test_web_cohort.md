
<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Web Cohort Tests

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/test_web_cohort
- Dependencies: [[Odoo 19/Enterprise Addons/web_cohort/web_cohort|web_cohort]]

## Summary

Web cohort Test

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `web.cohort.simple.model`
- `web.cohort.type`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Web Cohort Tests - Models and Relations
class "web.cohort.simple.model" as web_cohort_simple_model
class "web.cohort.type" as web_cohort_type
web_cohort_simple_model --> web_cohort_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
