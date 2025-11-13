<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Test Data Cleaning

- Version: v18
- Category: enterprise
- Source: enterprise18/test_data_cleaning
- Dependencies: [[Odoo 18/Enterprise Addons/data_cleaning/data_cleaning|data_cleaning]]

## Summary

Test Suite for Data Cleaning

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `data_cleaning.test.model`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Test Data Cleaning - Models and Relations
class "data_cleaning.test.model" as data_cleaning_test_model
class "res.country" as res_country
data_cleaning_test_model --> res_country : many2one
class "res.company" as res_company
data_cleaning_test_model --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
