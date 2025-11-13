<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Web Cohort Tests

- Version: v18
- Category: enterprise
- Source: enterprise18/test_web_cohort
- Dependencies: [[Odoo 18/Enterprise Addons/web_cohort/web_cohort|web_cohort]]

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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
